from django.contrib import admin

from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

    def set_books_unavailable(self, request, queryset):
        for book in queryset:
            book.availability = 0
            book.save()
