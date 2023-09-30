from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "user", "balance"]
        extra_kwargs = {
            "url": {"view_name": "wallet-detail", "lookup_field": "user"}
        }