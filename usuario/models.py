# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Perfil - Relacion con users
class Perfil(models.Model):
	numeroDocumento = models.CharField(max_length=15, unique=True,
		verbose_name="Número de Documento")
	telefono = PhoneNumberField(default='+573040000000',
		verbose_name="Teléfono")
	direccion = models.CharField(max_length=45, verbose_name="Dirección")
	user = models.OneToOneField(User, verbose_name="Usuario")

	def __unicode__(self):
		return self.user.username
