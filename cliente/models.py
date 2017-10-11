# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
	TIPO_CUENTA = (
		('corriente', 'Corriente'),
		('ahorros', 'Ahorros'),
		('recaudo','Recaudo'),
		)
	dni = models.CharField(primary_key=True, max_length=15,
		unique=True, verbose_name='Número de identificación')
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=100)
	telefono = PhoneNumberField(default='+570387260001',
		verbose_name='Teléfono')
	correo = models.EmailField(max_length=100, blank=True, null=True)
	ciudad = models.CharField(max_length=25, blank=True, null=True)
	direccion = models.CharField(max_length=100, blank=True, null=True,
		verbose_name='Dirección')
	banco = models.CharField(max_length=45, blank=True, null=True)
	tipoCuenta = models.CharField(choices=TIPO_CUENTA, max_length=25,
		blank=True, null=True, verbose_name='Tipo de cuenta')
	numeroCuenta = models.CharField(max_length=15, blank=True, null=True,
		verbose_name='Número de cuenta')

	def __unicode__(self):
		return self.dni
