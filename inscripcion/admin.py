'''
Created on 15/11/2013

@author: darwelx
'''
from inscripcion.models import Parentesco
from inscripcion.models import Nacionalidad
from inscripcion.models import Padre
from inscripcion.models import Madre
from inscripcion.models import Representante
from inscripcion.models import Escolaridad
from inscripcion.models import Materia
from inscripcion.models import Anio
from inscripcion.models import Seccion
from inscripcion.models import Estudiante
from inscripcion.models import Inscripcion
from django.contrib import admin


admin.site.register(Parentesco)
admin.site.register(Nacionalidad)
admin.site.register(Padre)
admin.site.register(Madre)
admin.site.register(Representante)
admin.site.register(Escolaridad)
admin.site.register(Materia)
admin.site.register(Anio)
admin.site.register(Seccion)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)