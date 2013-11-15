'''
Created on 15/11/2013

@author: darwelx
'''
from inscripcion.models import Parentesco
from inscripcion.models import Nacionalidad
from inscripcion.models import Padre
from django.contrib import admin


admin.site.register(Parentesco)
admin.site.register(Nacionalidad)
admin.site.register(Padre)
