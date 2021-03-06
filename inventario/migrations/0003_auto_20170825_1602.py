# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-25 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20170621_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='valorCompra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='valorIva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='valorVenta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
