from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from django.utils import timezone
from datetime import timedelta

def fecha_limite_mayor_que_hoy(value):
    if value <= timezone.now().date():
        raise ValidationError('La fecha límite debe ser mayor que la fecha de hoy.')
    
def fecha_recordatorio_mayor_que_hoy(value):
    if value < timezone.now().date():
        raise ValidationError('La fecha de recordatorio debe ser mayor o igual que hoy.')

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    fecha = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_recordatorio_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Evento: {self.nombre} - Día: {self.fecha}"

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_limite = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_recordatorio_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Tarea: {self.nombre} - Fecha Límite: {self.fecha_limite}"


class Pago(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    fecha_pago = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_limite_mayor_que_hoy])
    recordatorio = models.DateField(default=timezone.now().date() + timedelta(days=1), validators=[fecha_recordatorio_mayor_que_hoy])
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Pago: {self.nombre} - Valor: {self.valor} - Fecha Pago: {self.fecha_pago}"
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Contacto: {self.nombre} {self.apellido}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"




