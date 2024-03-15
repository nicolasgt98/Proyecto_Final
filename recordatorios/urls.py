from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [

#_________________________________________ Menú Principal
    path('', home, name = "home"),


#_________________________________________ Eventos
    path('eventos', EventoList.as_view(), name = "eventos"),



#_________________________________________ Tareas
    path('tareas', TareaList.as_view(), name = "tareas"),


#_________________________________________ Pagos
    path('pagos', PagoList.as_view(), name = "pagos"),


#_________________________________________ Buscar
#____________________ Eventos
    path('buscar_eventos/', buscar_eventos, name = "buscarEventos"),
    path('encontrar_eventos/', encontrar_eventos, name = "encontrarEventos"),

#____________________ Pagos
    path('buscar_pagos/', buscar_pagos, name = "buscarPagos"),
    path('encontrar_pagos/', encontrar_pagos, name = "encontrarPagos"),

#____________________ Tareas
    path('buscar_tareas/', buscar_tareas, name = "buscarTareas"),
    path('encontrar_tareas/', encontrar_tareas, name = "encontrarTareas"),


#_________________________________________ Sobre Mi
    path('sobre_mi/', sobre_mi, name = "sobreMi"),


#__________________________________________Abrir/Cerrar sesión, Autenticación y Registro 
    path('login/', login_request, name = "login"),
    path('logout/', LogoutView.as_view(template_name="recordatorios/logout.html"), name = "logout"),
] 