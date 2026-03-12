from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    #Registro
    #Cliente
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    #Coche
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    #Servicio --> OJO cambia la ruta
    path('servicios/crear/', crear_servicio, name='crear_servicio'),
    #Reparación
    path('reparacion/registrar/', registrar_reparacion, name='registrar_reparacion'),

    #Fetch de objetos dominio
    #Listar clientes
    path('clientes/', listar_clientes, name='lista_clientes'),
    #Cliente by ID
    path('clientes/<int:cliente_id>/', buscar_clienteById, name='buscar_cliente_id'),
    #Lista servcios
    path('servicios/', listar_servicios, name='listar_servicios'),
    #Buscar todos los coches de un cliente con sus respectivas reparaciones
    path('clientes/historial/<int:cliente_id>/', historial_cliente, name='historial_cliente_id'),
]