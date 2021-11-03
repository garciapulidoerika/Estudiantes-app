from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, default='')
    telefono = models.CharField(max_length=100, default='')
    correo = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre 