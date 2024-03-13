from django.urls import path, include
from .views import *

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


#_________________________________________ Buscar
    path('sobre_mi/', sobre_mi, name = "sobreMi"),
] 