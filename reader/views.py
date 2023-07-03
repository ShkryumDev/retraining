from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from reader.models import Reader
from serializers import ReaderSerializer
from tools.permissions.permissions import IsOwnerOrAdmin


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
