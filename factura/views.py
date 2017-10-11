#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
#importar http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
#Vistas
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.contrib.auth.models import User
from inventario.models import Inventario
from .models import Factura, DetalleFactura
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)
#pdf Dionicio
import datetime
#por defecto se instala html5lib==0.999999999
#para que funciones pip install html5lib==1.0b8
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
from django import http
import cgi
#modelos
from cliente.models import Cliente
from inventario.models import Inventario
import json
import decimal
from django.core import serializers
#para facturaCrear
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext as ctx
from django.template import Context
from .forms import RangoForm
from django.utils import timezone

#def facturaCrear(request):
#    return render(request, 'factura/crear_factura.html', {} )
@login_required()
@permission_required('factura.add_factura')
def facturaCrear(request):
    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print proceso
            print ("en try")
            if 'clienProv' not in proceso:
                msg = 'El cliente no ha sido seleccionado'
                raise Exception(msg)

            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)

            total = 0#factura cuando se crea inicia en 0

            for k in proceso['producto']:
                print (k['codigo'])
                producto = Inventario.objects.get(codigo=k['codigo'])
                subtotal = (producto.valorVenta) * int(k['cantidad'])
                total +=subtotal
                #print ("en for")
                print(k['cantidad'])
                print producto
                #print subtotal
                #print total

            crearFactura = Factura(
                cliente = Cliente.objects.get(dni=proceso['clienProv']),
                fecha = timezone.now(),
                total = total,
                vendedor = request.user,
                formaPago = proceso['tipoPago'],
                maquina = proceso['idMaquina'],
            )
            crearFactura.save()
            print "Factura Guardada"
            print crearFactura
            for k in proceso['producto']:
                producto = Inventario.objects.get(codigo=k['codigo'])
                print("en for detalle")
                print (producto)
                crearDetalle = DetalleFactura(
                    producto = producto,
                    descripcion = producto.descripcion,
                    cantidad = int(k['cantidad']),
                    valorIva = producto.valorIva,
                    precio = (producto.valorVenta - producto.valorIva) * int(k['cantidad']),
                    subtotal = producto.valorVenta * int(k['cantidad']),
                    factura = crearFactura,
                )
                crearDetalle.save()

                print("despues de crearDetalle.save()\n\n" )
            messages.success(request, 'La venta se ha realizado')
#ACA VOY
        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    return render(request, 'factura/crear_factura.html', {} )
    #return render_to_response('factura/crear_factura.html', {'form': form}, context_instance=RequestContext(request))




#Busqueda ajax de usuarios

def searchCliente(request):
    dni = request.GET.get('dni')
    dnis= Cliente.objects.filter(dni=dni)#__startswith
    dnis = [cliente_serializer(cliente) for cliente in dnis]
    return HttpResponse(json.dumps(dnis), content_type='application/json')

def cliente_serializer(cliente):
    return{'dni':cliente.dni, 'nombre':cliente.nombre,
           'apellidos':cliente.apellidos}

#productos
def searchProducto(request):
    codigo = request.GET.get('codigo')
    codigos = Inventario.objects.filter(codigo=codigo)
    json = serializers.serialize('json', codigos,
                                 fields= ('codigo', 'elemento',
                                 'valorIva', 'valorVenta'))
    return HttpResponse(json, content_type='application/json')




"""
def searchProducto(request):
    codigo = request.GET.get('codigo')
    codigos = Inventario.objects.filter(codigo__startswith=codigo)
    codigos = [producto_serializer(inventario) for inventario in codigos]
    return HttpResponse(json.dumps (codigos), content_type='application/json')

def producto_serializer(inventario):
    return{'codigo':inventario.codigo, 'elemento': inventario.elemento,
           'descripcion': inventario.descripcion,
           'valorVenta':inventario.valorVenta}
"""


def buscarProducto(request):
    busqueda = request.GET.get('serie')
    producto = Inventario.objects.filter(codigo=busqueda)
    data = serializers.serialize(
        'json', producto, fields=('codigo','elemento', 'cantidad',
                                  'valorIva', 'valorVenta'))
    return HttpResponse(data, content_type='application/json')

class FacturaInsert(LoginRequiredMixin,
                    PermissionRequiredMixin, CreateView):
    permission_required = ('factura.add_factura')
    model = Factura
    success_url = reverse_lazy('factura:detalle_factura_insert')
    fields = ['maquina','cliente','formaPago',]
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(FacturaInsert, self).form_valid(form)

class FacturaList(LoginRequiredMixin, ListView):
    #permission_required = ('factura.add_factura')
    model = Factura
    context_object_name = 'facturas'

class FacturaUpdate(LoginRequiredMixin,
                    PermissionRequiredMixin, UpdateView):
    permission_required = ('factura.change_factura')
    model = Factura
    success_url = reverse_lazy('factura:factura_list')
    fields = ['maquina', 'cliente', 'formaPago',]

@login_required()
@permission_required('factura.add_factura')
def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    template = loader.get_template('factura/factura_detail.html')
    context = {
        'factura' : factura
    }
    return HttpResponse(template.render(context, request))

#Funciones de Creacion de PDF
def write_pdf(template_src, context_dict):
    template = loader.get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),
                                 content_type = 'application/pdf')
    return http.HttpResponse('ocurrio un error al generar el reporte %s'% cgi.escape(html))

def Generar_pdf(request):
    ventas = Factura.objects.all()
    return write_pdf('factura/factura_all.html',
                     {'pagesize':'A4', 'ventas':ventas})
#Final de Funciones de Creacion de PDF legal

class PdfFactura(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ('factura.add_factura')
    def post(self, request, *args, **kwargs):
        buscar = request.POST['busqueda']
        print(buscar)
        ventas = DetalleFactura.objects.filter(factura=buscar).order_by("-producto")
        datoFactura = Factura.objects.filter(serie=buscar)
        return write_pdf('factura/factura_Detalle.html',
                         { 'ventas':ventas, 'pagesize':'A4', 'datoFactura':datoFactura})


class DetalleFacturaInsert(LoginRequiredMixin, CreateView):
    model = DetalleFactura
    success_url = reverse_lazy('factura:factura_list')
    fields = ['factura', 'producto', 'descripcion', 'cantidad']
    #facturaid = Factura.objects.filter(serie='11')


#funcion de ver el contenido de la factura por busqueda de serie
# class BuscarFactura(TemplateView)
#     def post(self, request, *args, **kwargs):
#         buscar = request.POST['busqueda']
#         print buscar

"""
#pdf
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, TA_CENTER
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib import colors
"""

"""
# class Generar_pdf(TemplateView):
#     def post(self, request, *args, **kwargs):
#         buscar = request.POST['busqueda']
#         ventas = Factura.objects.all()
#         return write_pdf('factura/factura_all.html',
#                          {'pagesize':'legal', 'ventas':ventas})

# Reporte Dinamico
class ReporteView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['busqueda']
        ventas = Factura.objects.all()
        return render(request, 'factura/factura_all.html',
                      {'ventas':ventas, 'factura':True})



#Report statico Reportlab
def report(request):
    #sabe que la funcion va responder un pdf
    response = HttpResponse(content_type='application/pdf')
    #se agrega el nombre de archivo y el conten-disposition para que se puyeda descargar del navegador
    response ['Content-Disposition'] = 'attachment; filename=Prueba_venta.pdf'
    #buffer de datos
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    # c.drawString(Izq_der, Abajo_arriba, 'texto')
    c.drawString(30, 750, 'Mayorista')
    c.setFont('Helvetica', 12)
    c.drawString(30,735, 'Report')
    c.setFont('Helvetica-Bold', 12)
    #fecha = datetime.datetime.now()
    c.drawString(480, 750, '20/10/2017' )
    c.line(460,747,560,747)

    #contenido estatico de tabla
    students = [{'#':'1', 'name':'Romario', 'b1':'4.5', 'b2':'4.8', 'b3':'5.0', 'total':'4.8'},
                {'#':'2', 'name':'Masha', 'b1':'3.0', 'b2':'3.8', 'b3':'3.5', 'total':'3.6'}]

    #tabla header
    #carga todos los estilos de la tabla
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    #Titulos de columna
    numero = Paragraph('''#''', styleBH)
    alumno = Paragraph(''' Alumno ''', styleBH)
    b1 = Paragraph(''' BIM1 ''', styleBH)
    b2 = Paragraph(''' BIM2 ''', styleBH)
    b3 = Paragraph(''' BIM3 ''', styleBH)
    total = Paragraph(''' TOTAL ''', styleBH)

    data = []
    #lista de la tabla con si
    #data.append = [[numero]]

    #tabla contenido
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7


    high = 650
    for student in students:
        this_student = [student['#'], student['name'], student['b1'], student['b2'], student['b3'], student['total']]
        data.append(this_student)
        high = high -18

    #escribir la tabla
    width, heigth = A4
    table = Table(data, colWidths = [1.9*cm, 9.5*cm, 1.9*cm, 1.9*cm, 1.9*cm, 1.9*cm])
    #Grilla de la tabla
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX',(0,0), (-1, -1), 0.25, colors.black), ]))

    #pdf size encapsularlo en el tamaño del A4 o tamaño de pagina
    table.wrapOn(c, width, heigth)
    table.drawOn(c, 30, high)
    c.showPage() #save page


    #guardar pdf
    c.save()
    #obtener valores de BytesIO del buffer y escribir en response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    #con el return descraga pdf
    return response
"""
