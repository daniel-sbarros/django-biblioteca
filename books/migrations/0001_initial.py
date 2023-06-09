# Generated by Django 4.1.7 on 2023-03-12 03:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('Terror', 'Terror'), ('FICÇÃO', 'Ficção'), ('ROMANCE', 'Romance'), ('DIDÁTICO', 'Didático'), ('OUTROS', 'Outros')], default='', max_length=100)),
                ('release_year', models.SmallIntegerField()),
                ('synopsis', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('registration_date', models.DateTimeField(default=datetime.datetime.now)),
                ('registration_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
