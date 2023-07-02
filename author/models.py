from django.db import models

from tools.same import DateTimeSame


class Author(DateTimeSame):
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    media = models.ImageField(upload_to='media/', null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
