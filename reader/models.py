from django.contrib.auth.models import User
from django.db import models

from reader.validators import PhoneNumberValidator
from tools.same import DateTimeSame


class Reader(DateTimeSame):
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=11, validators=[PhoneNumberValidator()], null=True, blank=False)
    is_active = models.BooleanField(default=True)
    books = models.ManyToManyField(to='book.Book')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def add_book(self, book):
        if self.books.count() < 3:
            self.books.add(book)
        else:
            raise Exception('Читатель не может взять больше трех книг')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
