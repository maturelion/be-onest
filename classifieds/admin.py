from django.contrib import admin
from .models import Classified, Photo


@admin.register(Classified)
class ClassifiedAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = [
        "id",
        "owner",
        "title",
        "country",
        "state",
        "city",
        "is_hot",
        "views",
        "created_at",
        "updated_at",
    ]
    search_fields = ["city"]
    list_filter = ["is_hot", "country__name"]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # date_hierarchy = "created_at"
    list_display = [
        "id",
        "user",
        "image",
    ]
    search_fields = ["user"]
    list_filter = ["user", "image"]
