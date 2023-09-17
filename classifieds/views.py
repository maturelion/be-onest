from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Classified
from .serializers import ClassifiedSerializer


class ClassifiedViewSet(ModelViewSet):
    queryset = Classified.objects.all()
    serializer_class = ClassifiedSerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country__name", "state__name", "city__name"]
