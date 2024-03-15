from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template import Template, Context
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import *

#___________________________________ Home
def home(request):
    return render(request, "recordatorios/home.html")

#___________________________________ Tareas
class TareaList(ListView): 
    model = Tarea

#___________________________________ Pagos
class PagoList(ListView): 
    model = Pago

#___________________________________ Eventos
class EventoList(ListView): 
    model = Evento




#___________________________________ Buscar
#__________________ Eventos
def buscar_eventos(request):
    return render(request, "recordatorios/buscar_evento.html")

def encontrar_eventos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        eventos = Evento.objects.filter(nombre__icontains = patron)
        contexto = {"evento_list": eventos}
        return render(request, "recordatorios/evento_list.html", contexto)
        
    class EventoList(ListView): 
        model = Evento

#__________________ Pagos
def buscar_pagos(request):
    return render(request, "recordatorios/buscar_pago.html")

def encontrar_pagos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        pagos = Pago.objects.filter(nombre__icontains = patron)
        contexto = {"pago_list": pagos}
        return render(request, "recordatorios/pago_list.html", contexto)
        
    class PagoList(ListView): 
        model = Pago

#__________________ Pagos
def buscar_tareas(request):
    return render(request, "recordatorios/buscar_tarea.html")

def encontrar_tareas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        tareas = Tarea.objects.filter(nombre__icontains = patron)
        contexto = {"tarea_list": tareas}
        return render(request, "recordatorios/tarea_list.html", contexto)
        
    class TareaList(ListView): 
        model = Tarea

#___________________________________ Sobre mi
def sobre_mi(request):
    return render(request, "recordatorios/sobre_mi.html")


#___________________________________ Abrir/Cerrar sesión, Autenticación y Registro 

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "recordatorios/home.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render (request, "recordatorios/login.html", {"form": miForm})