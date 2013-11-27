'''
Created on 26/11/2013

@author: darwelx
'''
from django import forms

class EstudianteForm(forms.Form):
    nacionalidad = forms.CharField(required=True)
    cedula = forms.CharField(required=True)
    nombres = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    lugar_nacimiento = forms.CharField(required=True)
    estado_nacimiento = forms.CharField(required=True)
    direccion_actual = forms.CharField(required=True)
    urbanizacion = forms.CharField(required=True)
    localidad = forms.CharField(required=True)
    estado = forms.CharField(required=True)
    email = forms.CharField(required=False)
    problema_fisico = forms.CharField(required=False)
    deporte_practica = forms.CharField(required=False)
    