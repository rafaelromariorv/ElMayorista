# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='valorIva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
