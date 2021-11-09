from rest_framework.serializers import ModelSerializer
from estudiantes.models import Estudiante

class DetalleEstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'