from rest_framework.viewsets import ModelViewSet
from estudiantes.serializers import DetalleEstudianteSerializer
from estudiantes.models import Estudiante

class EstudianteViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = DetalleEstudianteSerializer


