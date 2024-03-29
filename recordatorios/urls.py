from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [

#_________________________________________ Menú Principal
    path('', home, name = "home"),


#_________________________________________ Eventos
    path('eventos/', EventoList.as_view(), name='evento_list'),



#_________________________________________ Tareas
    path('tareas/', TareaList.as_view(), name = "tarea_list"),


#_________________________________________ Pagos
    path('pagos/', PagoList.as_view(), name = "pago_list"),


#_________________________________________ Pagos
    path('contactos/', ContactoList.as_view(), name = "contacto_list"),


#_________________________________________ Crear
#____________________ Eventos
    path('evento_crear', EventoCrear.as_view(), name = "evento_crear"),
#____________________ Tareas
    path('tarea_crear', TareaCrear.as_view(), name = "tarea_crear"),
#____________________ Pagos
    path('pago_crear', PagoCrear.as_view(), name = "pago_crear"),
#____________________ Pagos
    path('contacto_crear', ContactoCrear.as_view(), name = "contacto_crear"),


#_________________________________________ Actualizar
#____________________ Eventos
    path('evento_actualizar/<int:pk>/', EventoUpdate.as_view(), name = "evento_actualizar"),
#____________________ Tareas
    path('tarea_actualizar/<int:pk>/', TareaUpdate.as_view(), name = "tarea_actualizar"),
#____________________ Pagos
    path('pago_actualizar/<int:pk>/', PagoUpdate.as_view(), name = "pago_actualizar"),
#____________________ Contactos
    path('contacto_actualizar/<int:pk>/', ContactoUpdate.as_view(), name = "contacto_actualizar"),


#_________________________________________ Eliminar
#____________________ Eventos
    path('evento_eliminar/<int:pk>/', EventoDelete.as_view(), name = "evento_eliminar"),
#____________________ Tareas
    path('tarea_eliminar/<int:pk>/', TareaDelete.as_view(), name = "tarea_eliminar"),
#____________________ Pagos
    path('pago_eliminar/<int:pk>/', PagoDelete.as_view(), name = "pago_eliminar"),
#____________________ Contactos
    path('contacto_eliminar/<int:pk>/', ContactoDelete.as_view(), name = "contacto_eliminar"),


#_________________________________________ Buscar
#____________________ Eventos
    path('buscar_eventos/', buscar_eventos, name = "buscarEventos"),
    path('encontrar_eventos/', encontrar_eventos, name = "encontrarEventos"),
#____________________ Tareas
    path('buscar_tareas/', buscar_tareas, name = "buscarTareas"),
    path('encontrar_tareas/', encontrar_tareas, name = "encontrarTareas"),
#____________________ Pagos
    path('buscar_pagos/', buscar_pagos, name = "buscarPagos"),
    path('encontrar_pagos/', encontrar_pagos, name = "encontrarPagos"),
#____________________ Contactos
    path('buscar_contactos/', buscar_contactos, name = "buscarContactos"),
    path('encontrar_contactos/', encontrar_contactos, name = "encontrarContactos"),


#__________________________________________Abrir/Cerrar sesión, Autenticación y Registro 
    path('login/', login_request, name = "login"),
    path('logout/', LogoutView.as_view(template_name="recordatorios/login_logout_registro/logout.html"), name = "logout"),
    path('registrar/', register, name = "registrar"),


#_________________________________________ Mi Perfil
#____________________ Editar perfil
    path('editar_perfil/', editar_perfil, name = "editar_perfil"),
#____________________ Cambiar Clave
    path('<int:pk>/password/', CambiarClave.as_view(), name = "cambiar_clave"),
#____________________ Avatar
    path('agregar_avatar/', agregar_avatar, name = "agregar_avatar"),


#_________________________________________ Sobre Mi
    path('sobre_mi/', sobre_mi, name = "sobreMi"),


#_________________________________________ Contactame
    path('contactame/', contactame, name = "contactame"),
] 