from django.contrib import admin

from .models import Compra, DetalleCompra

@admin.register(Compra)
class AdminCompra(admin.ModelAdmin):
	list_display = ('serie', 'fecha', 
		'proveedor', 'formaPago','total','usuario')