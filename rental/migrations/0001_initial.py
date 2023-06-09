# Generated by Django 4.1.7 on 2023-03-12 19:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_alter_book_registration_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateTimeField(default=datetime.datetime.now)),
                ('rental_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rental_book', to='books.book')),
                ('rental_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rental_customer', to='customers.customer')),
                ('rental_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rental_registration_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
