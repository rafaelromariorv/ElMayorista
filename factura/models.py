# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cliente.models import Cliente
from inventario.models import Inventario
import decimal
from django.db.models import signals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.db import IntegrityError
import usuario.urls

class Factura(models.Model):
	FORMA_PAGO= (
		('efectivo', 'Efectivo'), ('cheque', 'Cheque'),
		('tarjeta débito', 'Tarjeta débito'),
		('tarjeta crédito', 'Tarjeta crédito'),
		('venta a crédito','Venta a crédito'), ('bono','Bono'),
		('vale','Vale'), ('otros','Otros'),
		)
	serie = models.AutoField(primary_key=True, auto_created=True,
		serialize=False)#codigo de factura
	maquina = models.CharField(max_length=20, verbose_name="Máquina")#N Seriemaquina
	fecha = models.DateField(auto_now_add=True)#fecha de Venta
	vendedor = models.ForeignKey(User)
	cliente = models.ForeignKey(Cliente)
	formaPago = models.CharField(choices=FORMA_PAGO ,
		max_length=50, verbose_name='Forma de pago')
	iva = models.DecimalField(max_digits=15, decimal_places=2, default=0,
		null=True, blank=True)
	total = models.DecimalField(max_digits=15, default=0,
		decimal_places=2, null=True, blank=True)
	def __str__(self):
		return str(self.serie)

	def subtotal(self):
		return self.total - self.iva


class DetalleFactura(models.Model):
	factura =models.ForeignKey(Factura, on_delete=models.CASCADE)
	producto = models.ForeignKey(Inventario)
	descripcion = models.CharField(max_length=45, verbose_name="Descripción")
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	cantidad = models.PositiveSmallIntegerField()
	valorIva = models.DecimalField(max_digits=15, decimal_places=2,
		verbose_name="Valor IVA")
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)

	def __unicode__(self):
		return self.descripcion

	def save(self, *args, **kwargs):
		try:
			consultaPrecio = Inventario.objects.get(elemento=self.producto)
			self.precio = round(float(consultaPrecio.valorVenta))
			self.valorIva = round(float(consultaPrecio.valorIva)*self.cantidad)
			self.subtotal = round(float(self.precio)*self.cantidad)
			consultaPrecio.cantidad -= self.cantidad
			consultaPrecio.save()
			consultaFactura = Factura.objects.get(serie = str(self.factura))
			consultaFactura.iva = round(float(consultaFactura.iva)) + round(float(self.valorIva))
			consultaFactura.total = round(float(consultaFactura.total))+ round(float(self.subtotal))
			consultaFactura.save()
			super(DetalleFactura, self).save(*args, **kwargs)
		except IntegrityError :
			return redirect('factura:factura_insert')
		else:
			pass

		super(DetalleFactura, self).save(*args, **kwargs)


# en ./manage.py shell
# from inventario.models import Inventario
# >>> producto = "cuchara soprera Tami"
# >>> precio = Inventario.objects.get(elemento=producto)
# >>> precio.cantidad
# 30
