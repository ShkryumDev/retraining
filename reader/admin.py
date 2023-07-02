from django.contrib import admin

from reader.models import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

    def toggle_active(self, request, queryset):
        for reader in queryset:
            reader.active = not reader.active
            reader.save()

    def delete_books_and_increase_count(self, request, queryset):
        for reader in queryset:
            book_count = reader.books.count()
            reader.books.all().delete()
            reader.book_count += book_count
            reader.save()
