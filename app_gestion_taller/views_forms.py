from django.shortcuts import render, redirect
from .models import *
from .forms import *

def formulario_registro_cliente(request):
    if request.method == 'POST':
        #Creamos un form con los datos recibidos
        form = ClienteForm(request.POST)
        #Validamos los datos recibidos
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_gestion_taller/formulario.html', {'titulo': 'Nuevo Cliente', 'form': form})

def formulario_registro_coche(request):
    if request.method == 'POST':
        #Creamos un form con los datos recibidos
        form = CocheForm(request.POST)
        #Validamos los datos recibidos
        if form.is_valid():
            form.save()
            return redirect('XXX')
    else:
        form = CocheForm()
    return render(request, 'app_gestion_taller/formulario.html', {'titulo': 'Nuevo Coche', 'form': form})

def formulario_registro_servicio(request):
    if request.method == 'POST':
        #Creamos un form con los datos recibidos
        form = ServicioForm(request.POST)
        #Validamos los datos recibidos
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    else:
        form = ServicioForm()
    return render(request, 'app_gestion_taller/formulario.html', {'titulo': 'Nuevo Servicio', 'form': form})