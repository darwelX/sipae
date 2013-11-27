# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from inscripcion.models import *
from inscripcion.forms import EstudianteForm

def inicio(request):
  mensaje="hola mundo"
  return render_to_response('index.html',locals(),RequestContext(request))
  
def inscripcion(request):
    nacionalidades = Nacionalidad.objects.all()
    estudiante = Estudiante()
    estudiante_encontrado = False
    mensaje_error = ""
    formEstudiante = EstudianteForm()
    
    if request.method == 'POST':
        
        if request.POST['procesarButton'] == 'Busccar':
            
            if request.POST['nacionalidad'] != '':
                n = Nacionalidad.objects.get(pk=int(request.POST['nacionalidad']))
                e = list(Estudiante.objects.filter(nacionalidad = n, cedula=request.POST['cedula']))
                if(len(e) > 0):
                    estudiante = e[0]
                    estudiante_encontrado = True
                else:
                    mensaje_error="Estudiante no encontrado"
            
        if request.POST['procesarButton'] == 'Siguiente':
                        
            if request.POST['id_estudiante'] == 'nuevo':
                formEstudiante = EstudianteForm(request.POST)
                
                if formEstudiante.is_valid():
                    print 'continuar'
                else:
                    print 'no puede continuar'
            else:
                estudiante_encontrado = True
                estudiante = Estudiante.objects.get(pk=int(request.POST['id_estudiante']))
                
    return render_to_response('inscripcion/inscripcion.html',locals(),RequestContext(request))