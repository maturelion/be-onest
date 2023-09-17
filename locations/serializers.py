from rest_framework import serializers
from .models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["url", "id", "name"]
        read_only_fields = ["name"]
        extra_kwargs = {
            "url": {"view_name": "country-detail", "lookup_field": "id"}}


class StateSerializer(serializers.ModelSerializer):
    country_set = CountrySerializer(read_only=True, source="country")

    class Meta:
        model = State
        fields = ["url", "id", "name", "country_set"]
        read_only_fields = ["name"]
        extra_kwargs = {
            "url": {"view_name": "state-detail", "lookup_field": "id"}}


class CitySerializer(serializers.ModelSerializer):
    state_name = serializers.ReadOnlyField(source='state.name')
    country_name = serializers.ReadOnlyField(source='state.country.name')

    class Meta:
        model = City
        fields = ["url", "id", "name", "country_name", "state_name"]
        read_only_fields = ["name"]
        extra_kwargs = {
            "url": {"view_name": "city-detail", "lookup_field": "id"}}
