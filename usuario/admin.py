# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
	list_display = ('id','user','numeroDocumento',
		'telefono','direccion',)
