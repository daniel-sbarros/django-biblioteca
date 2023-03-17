# Generated by Django 4.1.7 on 2023-03-14 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_rental_return_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_period',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 22, 52, 47, 512584)),
        ),
    ]
