# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-21 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='tipoCuenta',
            field=models.CharField(choices=[('corriente', 'Corriente'), ('ahorros', 'Ahorros'), ('recaudo', 'Recaudo')], max_length=25),
        ),
    ]
