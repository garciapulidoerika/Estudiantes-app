from django.db import models
from estudiantes.models import Estudiante

# Create your models here.
class Clase(models.Model):
    Materia = models.CharField(max_length=100)
    
    Inscritos = models.ManyToManyField(Estudiante, related_name='clases')

    def __str__(self):
        return self.Materia 

