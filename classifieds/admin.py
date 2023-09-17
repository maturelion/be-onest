from django.contrib import admin
from .models import Classified


@admin.register(Classified)
class ClassifiedAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = [
        "id",
        "title",
        "country",
        "state",
        "city",
        "is_hot",
        "created_at",
        "updated_at",
    ]
    search_fields = ["city"]
    list_filter = ["is_hot", "country__name"]
