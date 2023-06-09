# Generated by Django 4.1.7 on 2023-03-12 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='registration_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books_registration_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
