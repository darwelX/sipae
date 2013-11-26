# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from inscripcion.models import *


def inicio(request):
  mensaje="hola mundo"
  return render_to_response('index.html',locals(),RequestContext(request))
  
def inscripcion(request):
    nacionalidades = Nacionalidad.objects.all()
    estudiante = Estudiante()
    
    if request.method == 'POST':
        
        if request.POST['procesarButton'] == 'Busccar':
            n = Nacionalidad.objects.get(pk=int(request.POST['nacionalidad']))
            e = list(Estudiante.objects.filter(nacionalidad = n, cedula=request.POST['cedula']))
            if(len(e) > 0):
                estudiante = e[0]
            
            
    return render_to_response('inscripcion/inscripcion.html',locals(),RequestContext(request))