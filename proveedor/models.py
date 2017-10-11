# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Proveedor(models.Model):
	TIPO_CUENTA = (
		('corriente', 'Corriente'),
		('ahorros', 'Ahorros'),
		('recaudo','Recaudo'),
		)
	nit = models.CharField(max_length=15, unique=True)
	nombreEmpresa = models.CharField(max_length=45,
		verbose_name="Nombre de empresa")
	nombreRepresentante = models.CharField(max_length=45,
		verbose_name="Nombre de representante")
	apellidoRepresentante = models.CharField(max_length=45,
		verbose_name="Apellido de representante")
	telefonoUno = PhoneNumberField(default='+570387260001',
		verbose_name="Teléfono 1")
	telefonoDos = PhoneNumberField(default='+573040000001',
		verbose_name="Teléfono 2")
	correo = models.EmailField(max_length=100, blank=True, null=True)
	sitioWeb = models.CharField(max_length=100, blank=True, null=True,
		verbose_name="Sitio Web")
	ciudad = models.CharField(max_length=25)
	direccion = models.CharField(max_length=45)
	banco = models.CharField(max_length=45)
	tipoCuenta = models.CharField(choices=TIPO_CUENTA ,max_length=25,
		verbose_name="Tipo de cuenta")
	numeroCuenta = models.CharField(max_length=15, unique=True,
		verbose_name="Número de cuenta")

	def __unicode__(self):
		return self.nombreEmpresa
