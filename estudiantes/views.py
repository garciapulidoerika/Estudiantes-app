from django.shortcuts import render
from estudiantes.models import Estudiante
# Create your views here.

def estudiantes(request):

    nuevo = Estudiante.objects.create(nombre=request.POST['nombre'], direccion=request.POST['direccion'], telefono=request.POST['telefono'], correo=request.POST['correo'])
    print(nuevo)

    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes': estudiantes
    }

    return render(request, 'estudiantes/lista.html', contexto)

def estudiante_id(request, id):
    estudiante = Estudiante.objects.get(id=id)
    contexto={
        'estudiante': estudiante
    }
    return render(request, 'estudiantes/detalle.html', contexto)