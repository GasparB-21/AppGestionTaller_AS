# Create your views here.
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *


#Peticiones HTTP
from django.views.decorators.csrf import csrf_exempt
    
#Registro objetos dominio
#Cliente
@csrf_exempt
def registrar_cliente(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    #Parsemaos los datos 
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    nombre = data.get("nombre")
    telefono = data.get("telefono")
    email = data.get("email")

    #Validar entrada datos
    if not nombre or not telefono or not email:
        return JsonResponse({"error": "Faltan datos requeridos"}, status=400)
    #Si se valudan correctamente, se crea el cliente
    else:
        cliente = Cliente.objects.create(nombre=nombre, telefono=telefono, email=email)
        #Si no se especifica otra PK ORM creará un campo id q será autoincremental
        return JsonResponse({"message": "Cliente creado con éxito", "id": cliente.id, "nombre": cliente.nombre, "telefono": cliente.telefono, "email": cliente.email}, status=201)

@csrf_exempt 
def registrar_coche(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    #Parsemaos los datos 
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON inválido"}, status=400)

    #Obtenemos los datos del cliente
    cliente_id = data.get("cliente")
    marca = data.get("marca")
    modelo = data.get("modelo")
    matricula = data.get("matricula")

    #Validar entrada datos
    if not cliente_id or not marca or not modelo or not matricula:
        return JsonResponse({"error": "Faltan datos o el cliente indicado no está registrado"}, status=400)
    
    #Validamos existencia FK
    try:
        cliente = Cliente.objects.get(id=cliente_id)
    except Cliente.DoesNotExist:
        return JsonResponse({"error": "El cliente indicado no está registrado"}, status=400)

    #Si llegamos hasta aqui sin errores insertamos
    coche = Coche.objects.create(cliente=cliente, marca=marca, modelo=modelo, matricula=matricula)
    return JsonResponse({"message": "Coche creado con éxito", "cliente": coche.cliente.id, "marca": coche.marca, "modelo": coche.modelo, "matricula": coche.matricula}, status=201)
    
@csrf_exempt
def crear_servicio(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    #Parsemaos los datos 
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON inválido"}, status=400)

    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    #Validar entrada datos
    if not nombre or not descripcion:
        return JsonResponse({"error": "Faltan datos requeridos"}, status=400)
    else:
        servicio = Servicio.objects.create(nombre=nombre, descripcion=descripcion)
        return JsonResponse({"message": "Servicio creado con éxito", "id": servicio.id, "nombre": servicio.nombre, "descripcion": servicio.descripcion}, status=201)
    
@csrf_exempt
def registrar_reparacion(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    #Parsemaos los datos 
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    #Validamos los datos
    matricula_coche = data.get("coche")
    servicio_realizado = data.get("servicio")
    fecha_servicio = data.get("fecha_servicio")

    #Validar datos
    if not matricula_coche or not servicio_realizado or not fecha_servicio:
        return JsonResponse({"error": "Faltan datos o el coche / servicio seleccionado no está disponibls"}, status=400)
    
    #Validamos existencia FKs
    try:
        coche = Coche.objects.get(matricula=matricula_coche)
    except Coche.DoesNotExist:
        return JsonResponse({"error": "El coche indicado no está registrado"}, status=400)
    try:
        servicio = Servicio.objects.get(id=servicio_realizado)
    except Servicio.DoesNotExist:
        return JsonResponse({"error": "El servicio indicado no está registrado"}, status=400)
    
    reparacion = Reparacion.objects.create(coche=coche, servicio=servicio, fecha_servicio=fecha_servicio)
    return JsonResponse({"message": "Reparación registrada con éxito  con éxito", "id": reparacion.id, "coche": matricula_coche, "servicio": servicio_realizado, "fecha_reparacion": reparacion.fecha_servicio}, status=201)


#Fetch --> No se va a mostrar el mensaje de "Método no permitido pq no tengo el @csrf_exempt"
#Listar clientes
def listar_clientes(request):
    if request.method != "GET":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
    try:
        #listaClientes = list(Cliente.objects.values("id", "nombre", "telefono", "email"))
        #safe = false --> permite serializar tipos de datos que no son diccionarios, principalmente listas, facilitando el envío de arrays de objetos JSON. 
        #Por defecto, safe=True solo permite diccionarios para evitar vulnerabilidades de seguridad en navegadores antiguos
        #return JsonResponse(listaClientes, safe=False)

        listaClientes = Cliente.objects.all()
        dirClientes = {'clientes': listaClientes}
        return render(request, 'app_gestion_taller/lista_clientes.html', dirClientes)
    except Cliente.DoesNotExist:
        return JsonResponse({"message": "No hay clientes registrados"}, status=404)


#Cliente por id
def buscar_clienteById(request, cliente_id):
    if request.method != "GET":
        return JsonResponse({"error": "Método no permitido"}, status=405)
     
    try:
        #cliente = Cliente.objects.values("id", "nombre", "telefono", "email").get(id=cliente_id)
        #return JsonResponse(cliente, safe=False)

        cliente = Cliente.objects.all().get(id = cliente_id)
        coches = Coche.objects.filter(cliente=cliente)
        dirCliente = {
                        'cliente': cliente,
                        'coches': coches
                     }
        return render(request, 'app_gestion_taller/info_cliente.html', dirCliente)
    except Cliente.DoesNotExist:
        return JsonResponse({"message": "El cliente filtrado no existe."}, status=404)

#Listar servicios
def listar_servicios(request):
    if request.method != "GET":
        return JsonResponse({"error": "Método no permitido"}, status=405)
     
    try:
        #listaServicios = list(Servicio.objects.values("id", "nombre", "descripcion"))
        #return JsonResponse(listaServicios, safe=False)

        listaServicios = Servicio.objects.all()
        dirServicios = {'servicios': listaServicios}
        return render(request, 'app_gestion_taller/lista_servicios.html', dirServicios)

    except Servicio.DoesNotExist:
        return JsonResponse({"message": "No hay reparaciones disponibles"}, status=404)
    
#Historial cliente
#EXTRA: Mejorar eficiencia búsqueda
def historial_cliente(request, cliente_id):
    if request.method != "GET":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
    #Filtramos cliente
    try:
        clienteFiltrado = Cliente.objects.values("id", "nombre", "telefono", "email").get(id=cliente_id)
    except Cliente.DoesNotExist:
        return JsonResponse({"message": "El cliente filtrado no existe."}, status=404)
    
    #Filtramos los coches del cliente
    listaCocheCliente = list(Coche.objects.filter(cliente__id=cliente_id)
                                              .values("marca", "modelo", "matricula"))
    
    #Definimos el diccionario q vamos a usar en las respuestas
    historialCliente = {
        "cliente": clienteFiltrado,
        "coches": listaCocheCliente
    }
    
    if not listaCocheCliente:
        #return JsonResponse({"cliente": clienteFiltrado, "message": "El cliente no tiene coches registrados."}, status=404)
        return render(request, 'app_gestion_taller/info_historial_cliente.html', historialCliente) 
    
    for cocheFiltrado in listaCocheCliente:
        reparaciones = Reparacion.objects.select_related('servicio').filter(coche_id=cocheFiltrado["matricula"])

        #Formatemos como queremos añadir la info al JSON
        #Añadimos reparaciones serializables al dict del coche
        cocheFiltrado["reparaciones"] = [
            {
                "nombre": r.servicio.nombre,
                "descripcion": r.servicio.descripcion,
                "fecha_reparacion": str(r.fecha_servicio),
            }
            for r in reparaciones
        ]

    

    return render(request, 'app_gestion_taller/info_historial_cliente.html', historialCliente)
    #return JsonResponse(respuesta, safe=True)