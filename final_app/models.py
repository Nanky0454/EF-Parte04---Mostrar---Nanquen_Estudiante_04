from django.db import models
from datetime import datetime


# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length = 150)
    nombre = models.CharField(max_length = 150)
    precio_compra = models.FloatField(max_length = 150)
    precio_venta = models.FloatField(max_length = 150)
    fecha_compra = models.DateField()
    fecha_registro = models.DateField(default=datetime.now())
    estado = models.CharField(max_length = 15)