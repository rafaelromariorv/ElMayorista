# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0006_auto_20170825_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='valorIva',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor IVA'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]
