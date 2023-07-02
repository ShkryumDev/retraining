from django.db import models

from tools.same import DateTimeSame


class Book(DateTimeSame):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    count_page = models.PositiveIntegerField(null=False, blank=False)
    author = models.ForeignKey('author.Author', on_delete=models.RESTRICT, null=False)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.author}'

    def is_available(self):
        return self.available_copies > 0

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    