from rest_framework.serializers import ModelSerializer
from .models import Deposit


class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            "id",
            "user",
            "amount",
            "status",
            "address_used",
            "tx_hash",
            "ref_number",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "amount",
            "status",
            "address_used",
            "tx_hash",
            "ref_number",
        ]
        extra_kwargs = {
            "url": {"view_name": "deposit-detail", "lookup_field": "id"}}
