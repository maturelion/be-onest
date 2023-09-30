from django.contrib import admin
from .models import Wallet
from import_export.admin import ImportExportModelAdmin


class WalletAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["user__username"]
    list_display = ["user", "balance"]


admin.site.register(Wallet, WalletAdmin)