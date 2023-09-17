from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = "id"


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["state__country", "state"]
