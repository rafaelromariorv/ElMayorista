# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class AdminProovedor(admin.ModelAdmin):
	list_display = ('nit','nombreEmpresa','ciudad',
		'direccion','banco','tipoCuenta','numeroCuenta',)
