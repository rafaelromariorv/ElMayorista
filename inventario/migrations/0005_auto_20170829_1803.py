# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20170825_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='valorCompra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Valor de compra'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='valorIva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='valorVenta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Valor de venta'),
        ),
    ]
