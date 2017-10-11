# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_auto_20170711_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
