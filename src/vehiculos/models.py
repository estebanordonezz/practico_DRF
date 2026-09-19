from django.db import models

# Create your models here.

class Equipamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.IntegerField()
    color = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    kilometraje = models.IntegerField()
    fecha_carga = models.DateTimeField(auto_now_add=True)

    equipamientos = models.ManyToManyField(
        Equipamiento, related_name="vehiculos", blank=True
    )

    def __str__(self):
        return f"Tipo de vehiculo: {self.tipo_vehiculo} - Marca: {self.marca} - Modelo: {self.modelo}"

