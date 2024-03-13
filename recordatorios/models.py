from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

def fecha_limite_mayor_que_hoy(value):
    if value <= timezone.now():
        raise ValidationError('La fecha límite debe ser mayor que la fecha de hoy.')

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_limite = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

class Pago(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    fecha_pago = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateTimeField(default=datetime.now() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)



