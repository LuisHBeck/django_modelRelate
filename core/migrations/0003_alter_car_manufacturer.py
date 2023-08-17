# Generated by Django 4.2.4 on 2023-08-17 11:27

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_car_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=models.SET(core.models.set_default_automaker), to='core.automaker'),
        ),
    ]