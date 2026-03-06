from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

#La PK será la matricula y no el valor autogenerado por ORM
class Coche(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"
    
class Servicio(models.Model):
    #DUDA: Cual es el objetivo de este campo si ya mantenemos la relacion entre los coches y los servicios prestados a cada uno en la table reparaciones??
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
