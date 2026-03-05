from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Coche(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"
    
class Servicio(models.Model):
    #Este campo no es prescindibles si ya tenemos la tabla de abajo??
    #coches = models.ManyToManyField(Coche, through='CocheServicio')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Reparacion(models.Model):
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_servicio = models.DateField()     #fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.coche} - {self.servicio} ({self.fecha_servicio})"
