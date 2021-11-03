from django.shortcuts import render
from clase.models import Clase

# Create your views here.

def clases(request):

    clases = Clase.objects.all()
    contexto = {
        'clases': clases
    }

    return render(request, 'clases/listamaterias.html', contexto)

def clase_id(request, id):
    clase = Clase.objects.get(id=id)
    contexto={
        'clase': clase
    }
    return render(request, 'clases/detallemateria.html', contexto)