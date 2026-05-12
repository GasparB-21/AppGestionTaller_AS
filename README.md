# AppGestionTaller_AS
Aplicación para la gestión de un taller de coches creada en las clases de la asignatura de Arquitectura del Software.

Esta app permite registrar y consultar clientes, coches, servicios y reparaciones del taller. Los datos pueden gestionarse mediante vistas que devuelven listados y formularios web para crear nuevos registros.

## Acceso a la aplicación
La aplicación principal está montada bajo el prefijo `/gestion/`. Si el servidor Django se ejecuta en `http://localhost:8000/`, las rutas disponibles son:

- `http://localhost:8000/gestion/clientes/registrar/` — registrar un nuevo cliente
- `http://localhost:8000/gestion/coches/registrar/` — registrar un nuevo coche
- `http://localhost:8000/gestion/servicios/crear/` — crear un nuevo servicio
- `http://localhost:8000/gestion/reparacion/registrar/` — registrar una nueva reparación
- `http://localhost:8000/gestion/clientes/` — listar clientes
- `http://localhost:8000/gestion/clientes/<cliente_id>/` — ver datos de un cliente por ID
- `http://localhost:8000/gestion/servicios/` — listar servicios
- `http://localhost:8000/gestion/clientes/historial/<cliente_id>/` — buscar el historial de coches y reparaciones de un cliente
- `http://localhost:8000/gestion/clientes/nuevo/` — formulario para registrar un cliente
- `http://localhost:8000/gestion/coche/nuevo/` — formulario para registrar un coche
- `http://localhost:8000/gestion/servicio/nuevo/` — formulario para registrar un servicio

También está disponible el panel de administración de Django en:

- `http://localhost:8000/admin/`
