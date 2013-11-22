# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def inicio(request):
  mensaje="hola mundo"
  return render_to_response('index.html',locals(),RequestContext(request))
  
def inscripcion(request):
    return render_to_response('inscripcion/inscripcion.html',locals(),RequestContext(request))