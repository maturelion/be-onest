from rest_framework.serializers import ModelSerializer
from locations.serializers import CountrySerializer, StateSerializer, CitySerializer
from .models import Classified


class ClassifiedSerializer(ModelSerializer):
    # country_set = CountrySerializer(read_only=True, source="country")
    # state_set = StateSerializer(read_only=True, source="state")
    city_set = CitySerializer(read_only=True, source="city")
    class Meta:
        model = Classified
        fields = [
            "url",
            "id",
            "owner",
            "title",
            "description",
            "country",
            "state",
            "city",
            "city_set",
            "photos",
            "is_hot",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "url": {"view_name": "classified-detail", "lookup_field": "id"}}
