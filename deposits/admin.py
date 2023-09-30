from django.contrib import admin
from .models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "amount",
        "status",
        "address_used",
        "tx_hash",
        "ref_number",
        "created_at",
        "updated_at",
    ]
    search_fields = ["address_used", "ref_number"]
    list_filter = ["status"]
