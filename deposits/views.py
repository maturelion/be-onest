from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Deposit
from .serializers import DepositSerializer
from .blockcypher import BlockcypherWallet
from django.db import transaction
from wallets.models import Wallet
from utils.utils import get_ticker_price

import blockcypher
import environ

env = environ.Env()


class DepositViewSet(ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    lookup_field = "id"

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]

    def perform_create(self, serializer):
        with transaction.atomic():
            # generate address and subscribe to web hook
            blockcypher = BlockcypherWallet()
            address = blockcypher.generate_address()
            hook = blockcypher.deposit_webhook(address["address"])

            # create and save deposit
            deposit = serializer.save()
            # deposit.user = self.request.user
            deposit.address_used = address["address"]
            deposit.wallet = address
            deposit.ref_number = hook
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def deposit_webhook(request):
    data = request.data
    print(data)
    deposit = Deposit.objects.get(address_used=data["addresses"][0])
    wallet = Wallet.objects.get(user=deposit.user)
    value = data['total'] - data['fees']
    price_in_usd = value * float(get_ticker_price()["price"])

    if data["confirmations"] == 0:
        deposit.tx_hash = data["hash"]
        deposit.save()

    if data["confirmations"] >= 1 and deposit.status != "SUCCESSFUL" and data["double_spend"] == False:
        deposit.status = "SUCCESSFUL"
        deposit.amount = price_in_usd
        deposit.save()
        wallet.balance += price_in_usd
        wallet.save()

    if data["confirmations"] == int(env("CONFIRMATIONS")):
        blockcypher = BlockcypherWallet()
        blockcypher.unsubscribe_from_webhook(deposit.ref_number)

    return HttpResponse("OK", status=200)
