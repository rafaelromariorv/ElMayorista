# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^proveedor/new', views.ProveedorInsert.as_view(),
	name="proveedor_insert"),
	url(r'^proveedor/list$', views.ProovedorList.as_view(),
		name='proveedor_list'),
	url(r'^proveedor/(?P<pk>[0-9]+)/$', views.proveedor_detail,
    	name="proveedor_detail"),
	url(r'^proveedor/edit(?P<pk>[0-9]+)/$',views.ProveedorUpdate.as_view(),
		name='proveedor_edit'),
	 url(r'^proveedor/delete(?P<pk>[0-9]+)/$', views.ProveedorDelete.as_view(),
	 	name="proveedor_delete"),
	url(r'^proveedor/buscar$', views.BuscarView.as_view(), name='buscar'),
	url(r'^proveedor/search$', views.search, name='search'),
	#url(r'^proveedor/ajax$', views.BusquedaAjax.as_view(), name='search_Ajax'),
	#url(r'^proveedor/busqueda', views.Busqueda.as_view(),
	#name="proveedor_ajax"),
	#url(r'^proveedor/busqueda_ajax/$',views.BusquedaAjax),
		#name = 'buscar_ajax'),

	#url(r'^proveedor/busqueda_ajax$', BusquedaAjax.as_view(), name='buscar_ajax'),
]
