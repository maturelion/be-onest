from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Classified
from .serializers import ClassifiedSerializer


class ClassifiedViewSet(ModelViewSet):
    queryset = Classified.objects.all()
    serializer_class = ClassifiedSerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country__name", "state__name", "city__name", "owner"]

    def perform_create(self, serializer):
        classified = serializer.save()

        # Get the list of photo IDs from the request data
        photo_ids = self.request.data.get('photos', [])

        # Associate the selected photos with the ad
        for photo_id in photo_ids:
            try:
                photo = Photo.objects.get(id=photo_id)
                classified.photos.add(photo)
            except Photo.DoesNotExist:
                pass  # Handle the case where the photo doesn't exist

        return Response(serializer.data, status=status.HTTP_201_CREATED)
