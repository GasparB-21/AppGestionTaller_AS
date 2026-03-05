from django.contrib import admin
from .models import Cliente, Coche, Servicio, Reparacion

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Coche)
admin.site.register(Servicio)
admin.site.register(Reparacion)