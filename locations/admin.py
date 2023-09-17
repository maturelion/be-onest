from django.contrib import admin
from .models import Country, State, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', "country"]
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', "state"]
    search_fields = ['name', "state__name"]
