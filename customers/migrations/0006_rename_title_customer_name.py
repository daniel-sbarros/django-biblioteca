# Generated by Django 4.1.7 on 2023-03-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_rename_name_customer_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='title',
            new_name='name',
        ),
    ]
