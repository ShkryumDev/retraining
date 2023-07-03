from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from book.models import Book
from serializers import BookSerializer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


def perform_create(self, serializer):
    serializer.save()


def perform_update(self, serializer):
    serializer.save()


def perform_destroy(self, instance):
    instance.delete()
