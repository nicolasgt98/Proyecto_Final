from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Evento)
admin.site.register(Pago)
admin.site.register(Tarea)

