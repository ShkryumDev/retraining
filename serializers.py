from rest_framework import serializers

from author.models import Author
from book.models import Book
from reader.models import Reader


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'surname',
            'media',
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'description',
            'count_page',
            'author',
        ]


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = [
            'id',
            'name',
            'surname',
            'phone_number',
            'is_active',
            'books',
        ]
