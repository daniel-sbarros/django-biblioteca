# Generated by Django 4.1.7 on 2023-03-15 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_rental_delivered_alter_rental_return_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_period',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 11, 17, 54, 439660)),
        ),
    ]