from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#___________________________________ Home
def home(request):
    return render(request, "recordatorios/home.html")

#___________________________________ Eventos
class EventoList(LoginRequiredMixin, ListView): 
    model = Evento
    template_name = 'recordatorios/evento/evento_list.html'

#___________________________________ Tareas
class TareaList(LoginRequiredMixin, ListView): 
    model = Tarea
    template_name = 'recordatorios/tarea/tarea_list.html'

#___________________________________ Pagos
class PagoList(LoginRequiredMixin, ListView): 
    model = Pago
    template_name = 'recordatorios/pago/pago_list.html'

#___________________________________ Contactos
class ContactoList(LoginRequiredMixin, ListView): 
    model = Contacto
    template_name = 'recordatorios/contacto/contacto_list.html'


#___________________________________ Crear
#__________________ Eventos
class EventoCrear(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = 'recordatorios/evento/evento_form.html'
    fields = ["nombre", "lugar", "fecha", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("evento_list")

#__________________ Tareas
class TareaCrear(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = 'recordatorios/tarea/tarea_form.html'
    fields = ["nombre", "fecha_limite", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("tarea_list")

#__________________ Pago
class PagoCrear(LoginRequiredMixin, CreateView):
    model = Pago
    template_name = 'recordatorios/pago/pago_form.html'
    fields = ["nombre", "valor", "proveedor", "fecha_pago", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("pago_list")

#__________________ Contacto
class ContactoCrear(LoginRequiredMixin, CreateView):
    model = Contacto
    template_name = 'recordatorios/contacto/contacto_form.html'
    fields = ["nombre", "apellido", "correo", "telefono", "etiqueta", "descripcion"]
    success_url = reverse_lazy("contacto_list")


#___________________________________ Actualizar
#__________________ Eventos
class EventoUpdate(LoginRequiredMixin, UpdateView):
    model = Evento
    template_name = 'recordatorios/evento/evento_form.html'
    fields = ["nombre", "lugar", "fecha", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("evento_list")

#__________________ Tareas
class TareaUpdate(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = 'recordatorios/tarea/tarea_form.html'
    fields = ["nombre", "fecha_limite", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("tarea_list")

#__________________ Pago
class PagoUpdate(LoginRequiredMixin, UpdateView):
    model = Pago
    template_name = 'recordatorios/pago/pago_form.html'
    fields = ["nombre", "valor", "proveedor", "fecha_pago", "recordatorio", "etiqueta", "descripcion"]
    success_url = reverse_lazy("pago_list")


#__________________ Contacto
class ContactoUpdate(LoginRequiredMixin, UpdateView):
    model = Contacto
    template_name = 'recordatorios/contacto/contacto_form.html'
    fields = ["nombre", "apellido", "correo", "telefono", "etiqueta", "descripcion"]
    success_url = reverse_lazy("contacto_list")


#___________________________________ Eliminar
#__________________ Eventos
class EventoDelete(LoginRequiredMixin, DeleteView):
    model = Evento
    template_name = 'recordatorios/evento/evento_confirm_delete.html'
    success_url = reverse_lazy("evento_list")

#__________________ Tareas
class TareaDelete(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'recordatorios/tarea/tarea_confirm_delete.html'
    success_url = reverse_lazy("tarea_list")

#__________________ Pago
class PagoDelete(LoginRequiredMixin, DeleteView):
    model = Pago
    template_name = 'recordatorios/pago/pago_confirm_delete.html'
    success_url = reverse_lazy("pago_list")

#__________________ Contacto
class ContactoDelete(LoginRequiredMixin, DeleteView):
    model = Contacto
    template_name = 'recordatorios/contacto/contacto_confirm_delete.html'
    success_url = reverse_lazy("contacto_list")


#___________________________________ Buscar
#__________________ Eventos
@login_required
def buscar_eventos(request):
    return render(request, "recordatorios/buscar/buscar_evento.html")

@login_required
def encontrar_eventos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        eventos = Evento.objects.filter(nombre__icontains = patron)
        contexto = {"evento_list": eventos}
        return render(request, "recordatorios/evento/evento_list.html", contexto)
        
    class EventoList(ListView): 
        model = Evento

#__________________ Tareas
@login_required
def buscar_tareas(request):
    return render(request, "recordatorios/buscar/buscar_tarea.html")

@login_required
def encontrar_tareas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        tareas = Tarea.objects.filter(nombre__icontains = patron)
        contexto = {"tarea_list": tareas}
        return render(request, "recordatorios/tarea/tarea_list.html", contexto)
        
    class TareaList(ListView): 
        model = Tarea

#__________________ Pagos
@login_required
def buscar_pagos(request):
    return render(request, "recordatorios/buscar/buscar_pago.html")

@login_required
def encontrar_pagos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        pagos = Pago.objects.filter(nombre__icontains = patron)
        contexto = {"pago_list": pagos}
        return render(request, "recordatorios/pago/pago_list.html", contexto)
        
    class PagoList(ListView): 
        model = Pago


#__________________ Contactos
@login_required
def buscar_contactos(request):
    return render(request, "recordatorios/buscar/buscar_contacto.html")

@login_required
def encontrar_contactos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        contactos = Contacto.objects.filter(nombre__icontains = patron)
        contexto = {"contacto_list": contactos}
        return render(request, "recordatorios/contacto/contacto_list.html", contexto)
        
    class ContactoList(ListView): 
        model = Contacto


#___________________________________ Iniciar/Cerrar sesión, Autenticación y Registro 
#__________________ Login
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #____ Avatar
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "recordatorios/home.html")
        else:
            return redirect(reverse_lazy('login'))
            #____ Avatar
        
    else:
        miForm = AuthenticationForm()

    return render (request, "recordatorios/login_logout_registro/login.html", {"form": miForm})

#__________________ Resgistro
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:
        miForm = RegistroForm()

    return render (request, "recordatorios/login_logout_registro/registro.html", {"form": miForm})

#___________________________________ Mi Perfil
#__________________ Edición de Perfil
@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)

        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))

    else:
        miForm = UserEditForm(instance=usuario)

    return render (request, "recordatorios/mi_perfil/editar_perfil.html", {"form": miForm})

#__________________ Agregar Avatar
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatar_viejo = Avatar.objects.filter(user = usuario)
            if len(avatar_viejo) > 0:
                for i in range(len(avatar_viejo)):
                    avatar_viejo[i].delete()
            #___ Borrar avatares viejos
            avatar = Avatar(user=usuario, 
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = avatar.imagen.url
            request.session["avatar"] = imagen
            print(f"{imagen}")
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render (request, "recordatorios/mi_perfil/agregar_avatar.html", {"form": miForm})

#__________________ Cambiar Clave
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "recordatorios/mi_perfil/cambiar_clave.html"
    success_url = reverse_lazy("home")


#___________________________________ Sobre mi
def sobre_mi(request):
    return render(request, "recordatorios/sobre_mi.html")


#___________________________________ Contactame
def contactame(request):
    return render(request, "recordatorios/contactame.html")

