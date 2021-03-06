# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-25 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170825_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+570387260001', max_length=128, verbose_name='Tel\xe9fono'),
        ),
    ]
