from rest_framework.viewsets import ModelViewSet
from clase.serializers import DetalleClaseSerializer
from clase.models import Clase

class ClaseViewSet(ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = DetalleClaseSerializer

