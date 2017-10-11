# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('dni','nombre','apellidos',
		'telefono','correo',)
