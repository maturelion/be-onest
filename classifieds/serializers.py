from rest_framework.serializers import ModelSerializer
from locations.serializers import CountrySerializer, StateSerializer, CitySerializer
from .models import Classified, Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "user",
            "image"
        ]


class ClassifiedSerializer(ModelSerializer):
    # country_set = CountrySerializer(read_only=True, source="country")
    # state_set = StateSerializer(read_only=True, source="state")
    city_set = CitySerializer(read_only=True, source="city")
    photos_set = PhotoSerializer(many=True, read_only=True, source="photos")

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
            "photos_set",
            "is_hot",
            "views",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "url": {"view_name": "classified-detail", "lookup_field": "id"}}
