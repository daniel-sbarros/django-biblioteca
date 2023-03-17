from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    OPTIONS_CATEGORY = [
        ("Terror", "Terror"), ("FICÇÃO", "Ficção"), ("ROMANCE", "Romance"), ("DIDÁTICO", "Didático"), ('OUTROS','Outros')
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORY, default='')
    release_year = models.SmallIntegerField(null=False, blank=False)
    synopsis = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    registration_date = models.DateTimeField(default=datetime.now, blank=False)
    registration_user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='books_registration_user'
    )
    number_pages = models.SmallIntegerField(null=False, blank=False, default=0)

    def __str__(self) -> str:
        return self.title
