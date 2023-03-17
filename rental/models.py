from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

from books.models import Book
from customers.models import Customer

class Rental(models.Model):
    rental_customer = models.ForeignKey(
        to=Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='rental_customer'
    )

    rental_book = models.ForeignKey(
        to=Book,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='rental_book'
    )
    
    rental_date = models.DateTimeField(default=datetime.now, blank=False)
    return_period =  models.DateTimeField(default=(datetime.now() + timedelta(days=7)), blank=False)

    registration_user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='rental_registration_user'
    )

    amount_paid = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7, default=0.0)

    delivered = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self) -> str:
        return f'O cliente {self.rental_customer} alugou o livro {self.rental_book} na data {self.rental_date}'
