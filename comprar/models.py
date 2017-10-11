from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from proveedor.models import Proveedor
from inventario.models import Inventario

class Compra(models.Model):
	FORMA_PAGO= (
		('efectivo', 'Efectivo'), ('cheque', 'Cheque'),
		('tarjeta debito', 'Tarjeta debito'), ('tarjeta credito', 'Tarjeta credito'),
		('venta a credito','Venta a credito'), ('bono','Bono'),
		('vale','Vale'), ('otros','Otros'),
		)
	serie = models.CharField(max_length=30)
	fecha = models.DateField(auto_now_add=False)
	proveedor = models.ForeignKey(Proveedor)
	formaPago = models.CharField(choices=FORMA_PAGO ,
		max_length=50, verbose_name='Forma de pago')
	total = models.DecimalField(max_digits=8,
		decimal_places=2, null=True, blank=True)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.serie

class DetalleCompra(models.Model):
	compra =models.ForeignKey(Compra, on_delete=models.CASCADE)
	producto = models.ForeignKey(Inventario)
	descripcion = models.CharField(max_length=45)
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	cantidad = models.PositiveSmallIntegerField()
	valorIva = models.DecimalField(max_digits=6, decimal_places=2)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.producto



"""
no usar many to many hacerlo con puro foreing y tener un identificado de muchos

"""
