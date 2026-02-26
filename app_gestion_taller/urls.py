from django.contrib import admin
from .views import lista_clientes, detalle_cliente
from django.urls import path

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
]