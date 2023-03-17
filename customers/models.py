from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False, default='')
    address = models.CharField(max_length=150, null=False, blank=False)
    cep = models.CharField(max_length=20, null=False, blank=False, default='')
    city = models.CharField(max_length=20, null=False, blank=False, default='')
    document = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True, null=True)

    registration_date = models.DateTimeField(default=datetime.now, blank=False)
    registration_user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='customers_registration_user'
    )

    def __str__(self) -> str:
        return self.name.upper()
