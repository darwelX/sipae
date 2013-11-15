# -*- coding: utf-8 *-*
from django.db import models
from string import upper
# Create your models here.

''' Representa el parentesco entre un alumno y
    el representante '''
    
class Parentesco(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return upper(self.descripcion)
       
''' Representa la nacionalidad de una persona '''

class Nacionalidad(models.Model):
    letra = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=50)

    
    '''def __init__(self, letra, descripcion):
        self.letra = upper(letra)
        self.descripcion = descripcion
        models.Model.__init__(self)'''

           
    def __unicode__(self):
        return upper(self.letra)
    
''' Representa el padre de un determinado 
    Estudiante o alumno '''
        
class Padre(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.ForeignKey(Nacionalidad)
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tel_hab = models.CharField(max_length=15)
    tel_tra = models.CharField(max_length=15)
    tel_cel = models.CharField(max_length=15)
    
    def __unicode__(self):
        return "Sr {0} , {1}".format(self.apellidos,self.nombres)
    
''' Representa la madre de un determinado 
    Estudiante o alumno '''
        
class Madre(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.ForeignKey(Nacionalidad)
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tel_hab = models.CharField(max_length=15)
    tel_tra = models.CharField(max_length=15)
    tel_cel = models.CharField(max_length=15)
    
    def __unicode__(self):
        return "Sra {0} , {1}".format(self.apellidos,self.nombres)
    
''' Representante de un determinado 
    Estudiante o alumno '''
        
class Representante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.ForeignKey(Nacionalidad)
    cedula = models.CharField(max_length=15)
    email = models.EmailField(max_length=75)
    tel_hab = models.CharField(max_length=15)
    tel_tra = models.CharField(max_length=15)
    tel_cel = models.CharField(max_length=15)
    parentesco = models.ForeignKey(Parentesco)
    
    def __unicode__(self):
        return "{0} , {1}".format(self.apellidos,self.nombres)
''' Representa la escolaridad de un 
    Estudiante '''

class Escolaridad(models.Model):
    abreviatura = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "{0}".format(upper(self.abreviatura))
    
''' Representa una materia o asignatura
   '''

class Materia(models.Model):
    abreviatura=models.CharField(max_length=3)
    descripcion=models.CharField(max_length=100)

    def __unicode__(self):
        return "{0}".format(self.descripcion)
    
''' Representa el año a cursar para un
 determinado alumno '''
    
class Anio(models.Model):
    abreviatura=models.CharField(max_length=4)
    numero=models.IntegerField()
    materias=models.ManyToManyField(Materia)

    def __unicode__(self):
        return "{0}".format(self.abreviatura)
    
''' Representa Una Seccion en la cual
se puede inscribir un estudiante '''
    
class Seccion(models.Model):
    descripcion=models.CharField(max_length=2)
    matricula=models.IntegerField()
    matricula_actual=models.IntegerField()
    anio=models.ForeignKey(Anio)

    def __unicode__(self):
        return "{0}".format(self.descripcion)
    
''' Representa un Estudiante o Alumno de
la institucion '''
    
class Estudiante(models.Model):
    nacionalidad = models.ForeignKey(Nacionalidad)
    cedula = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    estado_nacimiento = models.CharField(max_length=100)
    direccion_actual = models.CharField(max_length=100)
    urbanizacion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    email = models.EmailField()
    problema_fisico = models.CharField(max_length=100)
    deporte_practica = models.CharField(max_length=100)
    padre = models.ForeignKey(Padre)
    madre = models.ForeignKey(Madre)
    representante = models.ForeignKey(Representante)
        
    def __unicode__(self):
        return "{0} , {1}".format(self.apellidos,self.nombres)
''' Representa la Inscripcion de un 
estudiante para un periodo escolar en especifico '''
   
class Inscripcion(models.Model):
    anio_escolar = models.CharField(max_length=15)
    plantel_procedencia = models.CharField(max_length=100)
    ubicacion_plantel_procedencia = models.CharField(max_length=100)
    tiene_otro_estudiante = models.CharField(max_length=2)
    anio_seccion_otro_estudiante = models.ManyToManyField(Seccion, null=True, related_name='anio_seccion_otro_estudiante')
    seccion = models.ForeignKey(Seccion, related_name='seccion')
    escolaridad = models.ForeignKey(Escolaridad)
    materia_pendiente = models.ManyToManyField(Materia, null=True, related_name='materia_pendiente')
    materia_repite = models.ManyToManyField(Materia, null=True, related_name='materia_repite')
    estudiante = models.ForeignKey(Estudiante)
    
    def __unicode__(self):
        return "{0}".format(self.anio_escolar)