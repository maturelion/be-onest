from rest_framework import viewsets
from .models import Wallet
from .serializers import WalletSerializer
from rest_framework.permissions import BasePermission

class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object or admin to view/edit it,
    but deny non-admin users from seeing the list of objects.
    """

    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    lookup_field = "user"
    filterset_fields = ('user',)
    http_method_names = ["get"]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user)
        return obj