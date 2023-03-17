# Generated by Django 4.1.7 on 2023-03-15 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_rental_amount_paid_alter_rental_return_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_period',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 11, 22, 29, 680733)),
        ),
    ]
