from rest_framework.serializers import ModelSerializer
from clase.models import Clase

class DetalleClaseSerializer(ModelSerializer):

    class Meta:
        model = Clase
        fields = '__all__'