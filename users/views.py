from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class UserViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"

    def get_object(self):
        obj = User.objects.get(slug=self.request.user.slug)
        return obj

    def update(self, request, *arg, **kwargs):
        user_object = self.get_object()
        data = request.data

        user_object.slug = slugify(data["username"])

        fields = user_object._meta.fields
        for field in fields:
            field = field.name.split(".")[-1]  # to get column name
            exec("user_object.%s = data.get(field, user_object.%s)" % (field, field))

        serializer_context = {
            "request": request,
        }

        user_object.save()

        serializer = UserSerializer(user_object, context=serializer_context)
        return Response(serializer.data)
