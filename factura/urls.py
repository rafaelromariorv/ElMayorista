# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^factura$',
    	TemplateView.as_view(template_name="factura/factura_index.html"),
    	name="factura"),
    url(r'^factura/new', views.FacturaInsert.as_view(),
    	name="factura_insert"),
    url(r'^factura/list$',views.FacturaList.as_view(),
        name='factura_list'),
    url(r'^factura/edit(?P<pk>[0-9]+)/$',views.FacturaUpdate.as_view(),
    	name='factura_edit'),
    url(r'^factura/(?P<pk>[0-9]+)/$', views.factura_detail,
		name="factura_detail"),
    url(r'^factura/detalle', views.DetalleFacturaInsert.as_view(),
    	name="detalle_factura_insert"),
    #url(r'^factura/detalle(?P<pk>[0-9]+)/$', views.DetalleFacturaInsert.as_view(),
    	#name="detalle_factura_insert_esp"),
    url(r'^factura/reporteAll', views.Generar_pdf, name='reporte_Facturas'),
    url(r'^factura/Pdf_Factura', views.PdfFactura.as_view(),
       name='reporte_Detalle_Factura'),
    url(r'^factura/venta$', views.facturaCrear,
        name="factura_venta"),
    url(r'^factura/search$', views.searchCliente, name='search_Cliente'),
    url(r'^factura/searchProducto$', views.searchProducto, name='search_Producto'),
    #prueba de reporte estatico con reportLab
    #url(r'^factura/report/$', views.report),
]
