# Generated by Django 4.2.4 on 2023-08-17 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
