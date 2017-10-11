#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Inventario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)


class InventarioInsert(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = ('inventario.add_inventario')
	model = Inventario
	success_url = reverse_lazy('inventario:inventario_list')
	fields = ['codigo', 'elemento', 'cantidad', 'descripcion',
	 'valorCompra', ]

class InventarioList(LoginRequiredMixin, ListView):
    #permission_required = ('inventario.add_inventario')
    model = Inventario
    context_object_name = 'elementos'

class InventarioUpdate(LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    permission_required = ('inventario.change_inventario')
    model = Inventario
    success_url = reverse_lazy('inventario:inventario_list')
    fields = ['codigo', 'elemento', 'cantidad', 'descripcion',
              'valorCompra', 'valorIva', 'valorVenta']

class InventarioDelete(LoginRequiredMixin,
                       PermissionRequiredMixin, DeleteView):
	permission_required= ('inventario.delete_inventario')
	model = Inventario
	success_url = reverse_lazy('inventario:inventario_list')

@login_required()
def inventario_detail(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    template = loader.get_template('inventario/inventario_detail.html')
    context = {
        'inventario' : inventario
    }
    return HttpResponse(template.render(context, request))
