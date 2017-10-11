# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,get_object_or_404
from .models import Proveedor
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy
#Permisos
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import login_required
import json

#---------------------Proveedor ---------------------------------
class ProveedorInsert(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = ('proveedor.add_proveedor')
	model = Proveedor
	success_url = reverse_lazy('proveedor:proveedor_list')
	fields = ['nit','nombreEmpresa','nombreRepresentante',
	'apellidoRepresentante','telefonoUno','telefonoDos',
	'correo','sitioWeb','ciudad','direccion','banco',
	'tipoCuenta','numeroCuenta',]

class ProovedorList(LoginRequiredMixin, PermissionRequiredMixin, ListView):#,
    permission_required= ('proveedor.add_proveedor')
    model = Proveedor
    context_object_name = 'proveedores'

class ProveedorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('proveedor.change_proveedor')
    model = Proveedor
    success_url = reverse_lazy('proveedor:proveedor_list')
    fields = ['nit','nombreEmpresa','nombreRepresentante',
              'apellidoRepresentante','telefonoUno','telefonoDos',
              'correo','sitioWeb','ciudad','direccion','banco',
              'tipoCuenta','numeroCuenta',]

class ProveedorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required= ('proveedor.delete_proveedor')
    model = Proveedor
    success_url = reverse_lazy('proveedor:proveedor_list')

@login_required()
def proveedor_detail(request, pk):
    #capturar id de reservaciones
    proveedor = get_object_or_404(Proveedor, pk=pk)
    #hacer iterable la relacion ManyToMany con el all
    #resources = reservation.resource.all()
    template = loader.get_template('proveedor/proveedor_detail.html')
    context = {
        'proveedor' : proveedor
    }
    return HttpResponse(template.render(context, request))

class BuscarView(LoginRequiredMixin, TemplateView):
    #funcion que se ejecuta con boton tiene Metodo Post
    def post(self, request, *args, **kwargs):
        buscar = request.POST['busqueda']
        print buscar
        #nombreEmpresa__ con dos rayas al piso para acceder al atributo
        busqueda = Proveedor.objects.filter(nombreEmpresa__contains=buscar)
        if busqueda:
            print ("ha preuntado por un proveedor")
            print busqueda
        else:
            busqueda = Proveedor.objects.filter(nombreRepresentante__contains=buscar)
            print busqueda
            print ("ha preuntado por un represntante")
        return render(request, 'proveedor/proveedor_buscar.html',
            {'busqueda' : busqueda, 'proveedor':True})
        #provedor nombre del model
        #busqueda el filter


#select * from proveedor where nombreEmpresa like '%Dev'
#proveedores = Proveedor.objects.filter(nombreEmpresa__startswhit=busqueda)
#@login_required()
def search(request):
    busqueda = request.GET.get('nombreEmpresa')#diccionario
    proveedores = Proveedor.objects.filter(nombreEmpresa__contains=busqueda)
    proveedores = [ proveedor_serializer(proveedor) for proveedor in proveedores]# Lista de diccionarios
    return HttpResponse(json.dumps(proveedores), content_type = 'aplication/json')

#@login_required()
def proveedor_serializer(proveedor):
    return {'id':proveedor.id,'nit':proveedor.nit, 'nombreEmpresa':proveedor.nombreEmpresa, 'nombreRepresentante': proveedor.nombreRepresentante}


"""
class Busqueda(ListView):
    model = Proveedor
    #Template_name = 'proveedor/proveedor_busquedaAjax.html'
    context_object_name = 'proveedores'

from django.core import serializers

def BusquedaAjax (request):
    print "fuera"
    if request.method == 'GET':
        print 'hola'

class BusquedaAjax(TemplateView):
    print "hola"
    def get(self, request, *args, **kwargs):
        print "En Get"
        id_proveedor = request.GET['id']
        print id_proveedor


        proveedor = Proveedor.objects.filter(proveedor__id = id_proveedor)
        data = serializers.serialize('json', proveedor,
            fields=('nombreEmpresa','nombreRepresentante'))
        return HttpResponse(data, mimetype='application/json')
        """
