# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Inventario

@admin.register(Inventario)
class AdminInventario(admin.ModelAdmin):
	list_display = ('codigo', 'elemento', 'cantidad',
		'descripcion', 'valorCompra', 'valorIva',
		'valorVenta',)
