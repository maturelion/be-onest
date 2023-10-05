from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Classified, Photo
from .serializers import ClassifiedSerializer
from wallets.models import Wallet
from django.db import transaction
import environ

env = environ.Env()


class ClassifiedViewSet(ModelViewSet):
    queryset = Classified.objects.all()
    serializer_class = ClassifiedSerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country__name", "state__name", "city__name", "owner"]
    parser_classes = (MultiPartParser, FormParser)

    def create(self, serializer):
        user_wallet = Wallet.objects.get(user=self.request.user)
        ads_overall_price = int(env("PRICE_PER_ADS"))

        if user_wallet.balance >= ads_overall_price:
            with transaction.atomic():
                classified = serializer.save()
                user_wallet.balance -= ads_overall_price
                user_wallet.save()
                # Get the list of photo from the request data
                photo_ids = self.request.data.getlist('photos', [])

                # Associate the selected photos with the ad
                for photo_id in photo_ids:
                    try:
                        photo = Photo.objects.create(
                            image=photo_id, user=self.request.user)
                        classified.photos.add(photo)
                    except Photo.DoesNotExist:
                        pass  # Handle the case where the photo doesn't exist
                print(user_wallet, "balance after")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Insufficient funds"}, status=status.HTTP_402_PAYMENT_REQUIRED)
