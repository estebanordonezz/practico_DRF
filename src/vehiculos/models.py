from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.IntegerField()
    color = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    kilometraje = models.IntegerField()
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tipo de vehiculo: {self.tipo_vehiculo} - Marca: {self.marca} - Modelo: {self.modelo}"

