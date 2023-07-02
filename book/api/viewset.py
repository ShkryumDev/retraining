from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from book.api.serializers import BookSerializer
from book.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser | permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
