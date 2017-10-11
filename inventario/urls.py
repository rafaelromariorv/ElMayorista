#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^inventario/new', views.InventarioInsert.as_view(),
		name="inventario_insert"),
	url(r'^inventario/list$', views.InventarioList.as_view(),
		name='inventario_list'),
	url(r'^inventario/edit(?P<pk>[0-9]+)/$', views.InventarioUpdate.as_view(),
    	name='inventario_edit'),
	 url(r'^inventario/delete(?P<pk>[0-9]+)/$', views.InventarioDelete.as_view(),
	 	name="inventario_delete"),
	url(r'^inventario/(?P<pk>[0-9]+)/$', views.inventario_detail,
		name="inventario_detail"),
]
