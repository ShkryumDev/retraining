from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from author.api.serializers import AuthorSerializer
from author.models import Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser | permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
