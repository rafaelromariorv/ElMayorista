# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^cliente/new', views.ClienteInsert.as_view(),
		name= "cliente_insert"),
	url(r'^cliente/list$', views.ClienteList.as_view(),
		name='cliente_list'),
	url(r'^cliente/edit(?P<pk>[0-9]+)/$',views.ClienteUpdate.as_view(),
		name='cliente_edit'),
	url(r'^cliente/delete(?P<pk>[0-9]+)/$', views.ClienteDelete.as_view(),
	 	name="cliente_delete"),
	url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detail,
		name="cliente_detail"),
]
