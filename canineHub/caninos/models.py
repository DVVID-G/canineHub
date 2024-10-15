from django.db import models

class Canino(models.Model):
    nombre = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    tamaño = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    multimedia = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
