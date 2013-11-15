# -*- coding: utf-8 *-*
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from inscripcion.models import *
import datetime

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
''' Test de la clase modelo Nacionalidad'''
                       
class NacionalidadTest(TestCase):
    
    def setUp(self):
        self.n1 = Nacionalidad(letra='V', descripcion='Venezolano')
        self.n1.save()
        
    def test_letra(self):
        self.assertEqual(self.n1.letra, 'V', "No coinciden las abreviaciones")
        self.assertEqual(self.n1.id, 1, "No coinciden los ids")
 
''' Test de la clase modelo Padre'''
                
class PadreTest(TestCase):
    
    def setUp(self):
        self.n1 = Nacionalidad(letra='V', descripcion='Venezolano')
        self.n1.save()
        self.p1= Padre(nombres='Darwel Alfonso',
                       apellidos="Quintero Duran",
                       nacionalidad=self.n1,
                       cedula='15686543',
                       empresa='BanfoAndes',
                       cargo='Programador',
                       email='darwel34@gmail.com',
                       tel_hab = '0277-5410938',
                       tel_tra = '0277-5410927',
                       tel_cel = '0414-5311345'
                       )
        self.p1.save()
        
    def test_datos(self):
        self.assertEqual(self.p1.id, 1, "(Padre)los ids no coinciden")
        self.assertEqual(self.p1.nacionalidad.letra, 'V',"(Padre)Nacionalidades no coinciden")
        self.assertEqual(self.p1.nacionalidad, self.n1, "(Padre)Objetos nacionalidad no son iguales")
        self.assertEqual(self.p1.nombres, 'Darwel Alfonso', "(Padre)nombres no coinciden")
        self.assertEqual(self.p1.apellidos, 'Quintero Duran', "(Padre)Apellidos no coinciden")
        self.assertEqual(self.p1.cedula, '15686543', "(Padre)cedulas no coinciden")
        self.assertEqual(self.p1.email,'darwel34@gmail.com',"(Padre)Emails no coinciden")
        self.assertEqual(self.p1.cargo,'Programador', '(Padre)Cargo no coincide')
        self.assertEqual(self.p1.empresa, 'BanfoAndes', '(Padre)empresas no coinciden')
        self.assertEqual(self.p1.tel_cel, '0414-5311345', '(Padre)telefonos de celular no coinciden')
        self.assertEqual(self.p1.tel_hab, '0277-5410938', '(Padre)telefonos de habitacion no coinciden')
        self.assertEqual(self.p1.tel_tra, '0277-5410927', '(Padre)telefonos de trabajo no coinciden')
        
    def test_consulta(self):
        padre = Padre.objects.get(pk=1)
        self.assertEqual(self.p1,padre,"Padre no encontrado")
        self.assertEqual(self.p1.cedula,padre.cedula, "(Padre)cedulas no coinciden")
        
''' Test de la clase modelo Madre'''
        
class MadreTest(TestCase):
    
    def setUp(self):
        self.n1 = Nacionalidad(letra='V', descripcion='Venezolano')
        self.n1.save()
        self.m1= Madre(nombres='Ingrid Coromoto',
                       apellidos="Mora Guerrero",
                       nacionalidad=self.n1,
                       cedula='15686544',
                       empresa='Leche Tachira',
                       cargo='Programador',
                       email='ingrid@gmail.com',
                       tel_hab = '0277-5410939',
                       tel_tra = '0277-5410928',
                       tel_cel = '0414-5311346'
                       )
        self.m1.save()
        
    def test_datos(self):
        self.assertEqual(self.m1.id, 1, "(Madre)los ids no coinciden")
        self.assertEqual(self.m1.nacionalidad.letra, 'V',"(Madre)Nacionalidades no coinciden")
        self.assertEqual(self.m1.nacionalidad, self.n1, "(Madre)Objetos nacionalidad no son iguales")
        self.assertEqual(self.m1.nombres, 'Ingrid Coromoto', "(Madre)nombres no coinciden")
        self.assertEqual(self.m1.apellidos, 'Mora Guerrero', "(Madre)Apellidos no coinciden")
        self.assertEqual(self.m1.cedula, '15686544', "(Madre)cedulas no coinciden")
        self.assertEqual(self.m1.email,'ingrid@gmail.com',"(Madre)Emails no coinciden")
        self.assertEqual(self.m1.cargo,'Programador', '(Madre)Cargo no coincide')
        self.assertEqual(self.m1.empresa, 'Leche Tachira', '(Madre)empresas no coinciden')
        self.assertEqual(self.m1.tel_cel, '0414-5311346', '(Madre)telefonos de celular no coinciden')
        self.assertEqual(self.m1.tel_hab, '0277-5410939', '(Madre)telefonos de habitacion no coinciden')
        self.assertEqual(self.m1.tel_tra, '0277-5410928', '(Madre)telefonos de trabajo no coinciden')
        
    def test_consulta(self):
        madre = Madre.objects.get(pk=1)
        self.assertEqual(self.m1,madre,"Madre no encontrada")
        self.assertEqual(self.m1.cedula,madre.cedula, "(Madre)cedulas no coinciden")        

''' Test de la clase modelo Parentesco '''
                
class ParentescoTest(TestCase):
    
    def setUp(self):
        self.pr1 = Parentesco(descripcion="Madre")
        self.pr1.save()
        
    def test_datos(self):
        self.assertEqual(self.pr1.id, 1, "Ids de parentesco no coinciden")
        self.assertEqual(self.pr1, Parentesco.objects.get(pk=1), "Objetos parentescos no coinciden")
        self.assertEqual(self.pr1.descripcion, 'Madre', "descripcion de parentesco no coinciden")

''' Test de la clase Representante '''

class TestRepresentante(TestCase):
    
    def setUp(self):
        self.n1 = Nacionalidad(letra='V', descripcion='Venezolano')
        self.n1.save()
        
        self.pr1 = Parentesco(descripcion="Madre")
        self.pr1.save()
        
        self.r1 = Representante(nombres='Maria Juana',
                       apellidos="Garcia Peña",
                       nacionalidad=self.n1,
                       parentesco=self.pr1,
                       cedula='15686548',
                       email='maria@gmail.com',
                       tel_hab = '0277-5410950',
                       tel_tra = '0277-5410930',
                       tel_cel = '0414-5311349'
                       )
        self.r1.save()
        
    def test_integridad(self):
        self.assertEqual(self.r1.id, 1, "Ids de representante no coinciden")
        self.assertEqual(self.r1.nacionalidad.id, 1, "ids de nacionalidad no coinciden")
        self.assertEqual(self.r1.parentesco.id, 1, "inds de pareentescco no coinciden")
        
    def test_datos(self):
        self.assertEqual(self.r1.nombres, "Maria Juana", "nombres no cinciden")
        self.assertEqual(self.r1.apellidos, "Garcia Peña", "apellidos no coinciden")
        self.assertEqual(self.r1.nacionalidad.letra, "V", "naccionalidad no coincide")
        self.assertEqual(self.r1.parentesco.descripcion, "Madre", "parentesco no cincide")
        self.assertEqual(self.r1.cedula, "15686548", "cedulas no coinciden")
        self.assertEqual(self.r1.email, "maria@gmail.com", "emails no coinciden")
        self.assertEqual(self.r1.tel_cel, "0414-5311349", "telfono celular no coincide")
        self.assertEqual(self.r1.tel_hab, "0277-5410950","telefono de habitacion no coinciden")
        self.assertEqual(self.r1.tel_tra, "0277-5410930", "telefono de trabajo no coinciden")

''' Test de la clase Escolaridad '''

class TestEscolaridad(TestCase):
    
    def setUp(self):
        self.escolaridad = Escolaridad(abreviatura='RG',descripcion='Regular')
        self.escolaridad.save()
        
    def test_integridad(self):
        self.assertEqual(self.escolaridad.id,1,"ids no coinciden")
        
    def test_datos(self):
        self.assertEqual(self.escolaridad.abreviatura, 'RG', 'abreviaturas no coinciden')
        self.assertEqual(self.escolaridad.descripcion, 'Regular', 'descripcion no coincide')

''' Test de la clase Materia '''
        
class TestMateria(TestCase):
    
    def setUp(self):
        self.materia = Materia(abreviatura='CL',descripcion='Castellano Y Literatura')
        self.materia.save()
        
    def test_integridad(self):
        self.assertEqual(self.materia.id, 1, 'ids no coinciden')
        
    def test_datos(self):
        self.assertEqual(self.materia.abreviatura, 'CL', 'abreviaturas no coinciden')
        self.assertEqual(self.materia.descripcion, 'Castellano Y Literatura', 'descripcion no coincide')
        
''' Test de la Clase Anio '''

class TestAnio(TestCase):
    
    def setUp(self):
        self.materia = Materia(abreviatura='CL',descripcion='Castellano Y Literatura')
        self.materia.save()
        self.anio = Anio(abreviatura='1ro',numero=1)
        self.anio.save()
        self.anio.materias.add(self.materia)
        self.anio.save()
        
    def test_integridad(self):
        self.assertEqual(self.anio.id, 1, 'ids no coinciden')
        self.assertEqual(self.anio.materias.all()[0].id, 1, 'ids de materia no coinciden')
        
    def test_datos(self):
        self.assertEqual(self.anio.abreviatura, '1ro', 'abreviaturas no coinciden')
        self.assertEqual(self.anio.numero,1,'numero de año no coincide')
        self.assertEqual(self.anio.materias.all()[0].abreviatura, 'CL', 'abreviatura de materia no coincide')
        self.assertEqual(self.anio.materias.all()[0].descripcion, 'Castellano Y Literatura', 'descripcion de materia no coincide')

''' Test de la clase Seccion ''' 
       
class TestSeccion(TestCase):
    
    def setUp(self):
        self.anio = Anio(abreviatura='1ro',numero=1)
        self.anio.save()
        self.seccion = Seccion(descripcion='A',matricula=45,matricula_actual=45,anio=self.anio)
        self.seccion.save()
        
    def test_integridad(self):
        self.assertEqual(self.seccion.id,1,"ids no coinciden")
        self.assertEqual(self.seccion.anio.id, 1, 'ids de año no coinciden')
        
    def test_datos(self):
        self.assertEqual(self.seccion.descripcion, 'A', 'descripcion de la seccion no coincide')
        self.assertEqual(self.seccion.matricula, 45, 'matricula no coinciden')
        self.assertEqual(self.seccion.matricula_actual, 45, 'matricula actual no coinciden')
        self.assertEqual(self.seccion.anio.abreviatura, '1ro', 'abreviatura de año no coinciden')
        self.assertEqual(self.seccion.anio.numero, 1, 'numero de año no coinciden')
        
''' Test de la clase Estudiante '''

class TestEstudiante(TestCase):
    
    def setUp(self):
        self.nacionalidad = Nacionalidad(letra='V', descripcion='Venezolano')
        self.nacionalidad.save()
        self.pr1 = Parentesco(descripcion="Madre")
        self.pr1.save()
        
        self.r1 = Representante(nombres='Maria Juana',
                       apellidos="Garcia Peña",
                       nacionalidad=self.nacionalidad,
                       parentesco=self.pr1,
                       cedula='15686548',
                       email='maria@gmail.com',
                       tel_hab = '0277-5410950',
                       tel_tra = '0277-5410930',
                       tel_cel = '0414-5311349'
                       )
        self.r1.save()
        self.m1= Madre(nombres='Ingrid Coromoto',
                       apellidos="Mora Guerrero",
                       nacionalidad=self.nacionalidad,
                       cedula='15686544',
                       empresa='Leche Tachira',
                       cargo='Programador',
                       email='ingrid@gmail.com',
                       tel_hab = '0277-5410939',
                       tel_tra = '0277-5410928',
                       tel_cel = '0414-5311346'
                       )
        self.m1.save()
        self.p1= Padre(nombres='Darwel Alfonso',
                       apellidos="Quintero Duran",
                       nacionalidad=self.nacionalidad,
                       cedula='15686543',
                       empresa='BanfoAndes',
                       cargo='Programador',
                       email='darwel34@gmail.com',
                       tel_hab = '0277-5410938',
                       tel_tra = '0277-5410927',
                       tel_cel = '0414-5311345'
                       )
        self.p1.save()
        self.estudiante= Estudiante(nacionalidad = self.nacionalidad,
                                    cedula='123456789',
                                    apellidos='Rojas Benitez',
                                    nombres='Alexandra Betzabe',
                                    sexo='F',
                                    fecha_nacimiento=datetime.date(1996,6,29),
                                    lugar_nacimiento='LAS MESAS',
                                    estado_nacimiento='TACHIRA',
                                    direccion_actual='CONJUNTO RESIDENCIAL MESA ALTA, CASA #19',
                                    urbanizacion='LAS MESAS',
                                    localidad='LAS MESAS',
                                    estado='TACHIRA',
                                    email='alexandra@gmail.com',
                                    problema_fisico='NINGUNO',
                                    deporte_practica='BOLAS CRIOLLAS',
                                    padre=self.p1,
                                    madre=self.m1,
                                    representante=self.r1)
        self.estudiante.save()
        
    def test_integridad(self):
        self.assertEqual(self.estudiante.nacionalidad.id, 1, 'ids de nacionalidad no coinciden')
        self.assertEqual(self.estudiante.madre.id, 1, 'id de madre no coincide')
        self.assertEqual(self.estudiante.padre.id,1,'id de padre no coincide')
        self.assertEqual(self.estudiante.representante.id,1,'id de representante no coincide')
        
    def test_datos(self):
        self.assertEqual(self.estudiante.cedula, '123456789', 'cedula de estudiante no coincide')
        self.assertEqual(self.estudiante.apellidos, 'Rojas Benitez','apellidos no coinciden')
        self.assertEqual(self.estudiante.nombres,'Alexandra Betzabe','nombres no coinciden')
        self.assertEqual(self.estudiante.sexo,'F','sexos no coinciden')
        self.assertEqual(self.estudiante.fecha_nacimiento.strftime('%Y-%m-%d'),'1996-06-29','fechas de nacimiento no coinciden')
        self.assertEqual(self.estudiante.lugar_nacimiento,'LAS MESAS','lugar de nacimiento no coinciden')
        self.assertEqual(self.estudiante.estado_nacimiento, 'TACHIRA', 'estado de nacimeinto no coinciden')
        self.assertEqual(self.estudiante.direccion_actual,'CONJUNTO RESIDENCIAL MESA ALTA, CASA #19','la direccion actual no coinciden')
        self.assertEqual(self.estudiante.urbanizacion, 'LAS MESAS', 'urbanizacion no coinciden')
        self.assertEqual(self.estudiante.localidad,'LAS MESAS','localidad no coinciden')
        self.assertEqual(self.estudiante.estado,'TACHIRA','estados no coinciden')
        self.assertEqual(self.estudiante.email,'alexandra@gmail.com','emails no coinciden')
        self.assertEqual(self.estudiante.problema_fisico,'NINGUNO','problema fisico no coinciden')
        self.assertEqual(self.estudiante.deporte_practica,'BOLAS CRIOLLAS','deporte que practica no coinciden')
        self.assertEqual(self.estudiante.nacionalidad.letra,'V','letra de nacionalidad no coincide')
        self.assertEqual(self.estudiante.nacionalidad.descripcion,'Venezolano','descripcion de nacionalidad no coincide')
        
    def test_datos_madre(self):
        self.assertEqual(self.estudiante.madre.cedula, '15686544', 'cedula de la madre no coincide')
        self.assertEqual(self.estudiante.madre.nombres, 'Ingrid Coromoto', 'nombres de la madre no coinciden')
        self.assertEqual(self.estudiante.madre.apellidos, 'Mora Guerrero', 'apellidos de la madre no coinciden')
        self.assertEqual(self.estudiante.madre.empresa, 'Leche Tachira', 'empresa no coinciden')
        self.assertEqual(self.estudiante.madre.cargo, 'Programador', 'cargo no coincide')
        self.assertEqual(self.estudiante.madre.email,'ingrid@gmail.com','email no coinciden')
        self.assertEqual(self.estudiante.madre.tel_hab, '0277-5410939', 'telefono de habitacion no coinciden')
        self.assertEqual(self.estudiante.madre.tel_tra, '0277-5410928', 'telefono de trabajo no coinciden')
        self.assertEqual(self.estudiante.madre.tel_cel,'0414-5311346','telefono celular no coincieden')
        
    def test_datos_padre(self):
        self.assertEqual(self.estudiante.padre.cedula, '15686543', 'cedula del padre no coincide')
        self.assertEqual(self.estudiante.padre.nombres, 'Darwel Alfonso', 'nombres del padre no coinciden')
        self.assertEqual(self.estudiante.padre.apellidos, 'Quintero Duran', 'apellidos del padre no coinciden')
        self.assertEqual(self.estudiante.padre.empresa, 'BanfoAndes', 'empresa no coinciden')
        self.assertEqual(self.estudiante.padre.cargo, 'Programador', 'cargo no coincide')
        self.assertEqual(self.estudiante.padre.email,'darwel34@gmail.com','email no coinciden')
        self.assertEqual(self.estudiante.padre.tel_hab, '0277-5410938', 'telefono de habitacion no coinciden')
        self.assertEqual(self.estudiante.padre.tel_tra, '0277-5410927', 'telefono de trabajo no coinciden')
        self.assertEqual(self.estudiante.padre.tel_cel,'0414-5311345','telefono celular no coincieden')
        
    def test_datos_representante(self):
        self.assertEqual(self.estudiante.representante.cedula,'15686548','la cedula del representante no coincide')
        self.assertEqual(self.estudiante.representante.nombres, 'Maria Juana', 'los nombres del representante no coinciden')
        self.assertEqual(self.estudiante.representante.apellidos, 'Garcia Peña', 'los apellidos del representante no coinciden')
        self.assertEqual(self.estudiante.representante.nacionalidad.letra,'V','la nacionalidad del representante no coinciden')
        self.assertEqual(self.estudiante.representante.parentesco.descripcion, 'Madre', 'el parentesco del representante no coincide')
        self.assertEqual(self.estudiante.representante.email, 'maria@gmail.com', 'el email del representante no coincide')
        self.assertEqual(self.estudiante.representante.tel_hab, '0277-5410950', 'el telefono de habitacion del representante no coincide')
        self.assertEqual(self.estudiante.representante.tel_tra, '0277-5410930', 'el telefono del trabajo del representante no coinciden')
        self.assertEqual(self.estudiante.representante.tel_cel, '0414-5311349', 'el telefono celular del representante no coincide')

''' Test de la clase Inscripcion '''
                
class TestInscripcion(TestCase):
    
    def setUp(self):
        self.nacionalidad = Nacionalidad(letra='V', descripcion='Venezolano')
        self.nacionalidad.save()
        self.pr1 = Parentesco(descripcion="Madre")
        self.pr1.save()
        
        self.r1 = Representante(nombres='Maria Juana',
                       apellidos="Garcia Peña",
                       nacionalidad=self.nacionalidad,
                       parentesco=self.pr1,
                       cedula='15686548',
                       email='maria@gmail.com',
                       tel_hab = '0277-5410950',
                       tel_tra = '0277-5410930',
                       tel_cel = '0414-5311349'
                       )
        self.r1.save()
        self.m1= Madre(nombres='Ingrid Coromoto',
                       apellidos="Mora Guerrero",
                       nacionalidad=self.nacionalidad,
                       cedula='15686544',
                       empresa='Leche Tachira',
                       cargo='Programador',
                       email='ingrid@gmail.com',
                       tel_hab = '0277-5410939',
                       tel_tra = '0277-5410928',
                       tel_cel = '0414-5311346'
                       )
        self.m1.save()
        self.p1= Padre(nombres='Darwel Alfonso',
                       apellidos="Quintero Duran",
                       nacionalidad=self.nacionalidad,
                       cedula='15686543',
                       empresa='BanfoAndes',
                       cargo='Programador',
                       email='darwel34@gmail.com',
                       tel_hab = '0277-5410938',
                       tel_tra = '0277-5410927',
                       tel_cel = '0414-5311345'
                       )
        self.p1.save()
        self.estudiante= Estudiante(nacionalidad = self.nacionalidad,
                                    cedula='123456789',
                                    apellidos='Rojas Benitez',
                                    nombres='Alexandra Betzabe',
                                    sexo='F',
                                    fecha_nacimiento=datetime.date(1996,6,29),
                                    lugar_nacimiento='LAS MESAS',
                                    estado_nacimiento='TACHIRA',
                                    direccion_actual='CONJUNTO RESIDENCIAL MESA ALTA, CASA #19',
                                    urbanizacion='LAS MESAS',
                                    localidad='LAS MESAS',
                                    estado='TACHIRA',
                                    email='alexandra@gmail.com',
                                    problema_fisico='NINGUNO',
                                    deporte_practica='BOLAS CRIOLLAS',
                                    padre=self.p1,
                                    madre=self.m1,
                                    representante=self.r1)
        self.estudiante.save()

        self.materiaCL = Materia(abreviatura='CL',descripcion='Castellano Y Literatura')
        self.materiaCL.save()
        
        self.materiaIN = Materia(abreviatura='IN',descripcion='Ingles')
        self.materiaIN.save()
                        
        self.anio = Anio(abreviatura='1ro',numero=1)
        self.anio.save()
        
        self.anio.materias.add(self.materiaCL,self.materiaIN)
        self.anio.save()
        
        self.seccionA = Seccion(descripcion='A',matricula=45,matricula_actual=45,anio=self.anio)
        self.seccionA.save()
        
        self.seccionB = Seccion(descripcion='B',matricula=45,matricula_actual=45,anio=self.anio)
        self.seccionB.save()
        
        self.escolaridad = Escolaridad(abreviatura='RG',descripcion='Regular')
        self.escolaridad.save()
        
        self.inscripcion = Inscripcion(anio_escolar='2011-2012',
                                       plantel_procedencia='Dr Antonio Romulo Costa',
                                       ubicacion_plantel_procedencia='La Fria Edo Tachira',
                                       tiene_otro_estudiante='SI',
                                       seccion=self.seccionA,
                                       escolaridad=self.escolaridad,
                                       estudiante=self.estudiante) 
        self.inscripcion.save()   
        
        self.inscripcion.materia_pendiente.add(self.materiaCL)
        self.inscripcion.materia_repite.add(self.materiaIN)
        self.inscripcion.anio_seccion_otro_estudiante.add(self.seccionB)
        
        self.inscripcion.save()           
        
    def test_integridad(self):
        self.assertEqual(1, self.inscripcion.id, 'los ids no coinciden')
        self.assertEqual(2, self.inscripcion.anio_seccion_otro_estudiante.all()[0].id, 'id de seccion en que estudia  otro estudiante no coinciden')
        self.assertEqual(1, self.inscripcion.seccion.id, 'id de seccion a inscribir no coinciden')
        self.assertEqual(1, self.inscripcion.escolaridad.id, 'id de escolaridad no coinciden')
        self.assertEqual(1, self.inscripcion.estudiante.id, 'id de estudiante a inscribir no coinciden')
        self.assertEqual(1, self.inscripcion.materia_pendiente.all()[0].id, 'id de materia pendiente no coinciden')
        self.assertEqual(2, self.inscripcion.materia_repite.all()[0].id, 'id de materia que repite no coinciden')
        
    def test_datos(self):
        self.assertEqual(self.inscripcion.anio_escolar, '2011-2012', 'el año escolar no coinciden')
        self.assertEqual(self.inscripcion.plantel_procedencia, 'Dr Antonio Romulo Costa', 'el plantel de procedencia no coinciden')
        self.assertEqual(self.inscripcion.ubicacion_plantel_procedencia, 'La Fria Edo Tachira', 'la ubicacion del plantel de procedencia no coinciden')
        self.assertEqual(self.inscripcion.tiene_otro_estudiante, 'SI', 'respuesta de otro estudiante no coinciden')
        self.assertEqual(self.inscripcion.anio_seccion_otro_estudiante.all()[0].descripcion, 'B', 'descripcion de la seccion no coinciden')
        self.assertEqual(self.inscripcion.anio_seccion_otro_estudiante.all()[0].matricula, 45, 'matricula de la seccion no coinciden')
        self.assertEqual(self.inscripcion.anio_seccion_otro_estudiante.all()[0].matricula_actual, 45, 'matricula actual de la seccion no coinciden')
        self.assertEqual(self.inscripcion.anio_seccion_otro_estudiante.all()[0].anio.abreviatura, '1ro', 'la abreviatura del año no coinciden')
        self.assertEqual(self.inscripcion.anio_seccion_otro_estudiante.all()[0].anio.numero, 1, 'el numero de año no coinciden')
        self.assertEqual(self.inscripcion.seccion.descripcion, 'A', 'descripcion de la seccion no coinciden')
        self.assertEqual(self.inscripcion.seccion.matricula, 45, 'la matricula de la seccion no coinciden')
        self.assertEqual(self.inscripcion.seccion.matricula_actual, 45, 'la matricula actual no coinciden')
        self.assertEqual(self.inscripcion.escolaridad.abreviatura, 'RG', 'la abreviatura de la escolaridad no coinciden')
        self.assertEqual(self.inscripcion.escolaridad.descripcion, 'Regular', 'la descripcion de la escolaridad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.nacionalidad.letra,'V','la letra de la nacionalida no coinciden')
        self.assertEqual(self.inscripcion.estudiante.nacionalidad.descripcion, 'Venezolano', 'la descripcion de la nacionalidad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.cedula, '123456789', 'la cedula del estudiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.apellidos, 'Rojas Benitez', 'los apellidos del estuddiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.nombres, 'Alexandra Betzabe', 'los nombres del estudiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.sexo, 'F', 'el sexo del estudiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.fecha_nacimiento.strftime('%Y-%m-%d'), '1996-06-29', 'la fecha de nacimiento no coinciden')
        self.assertEqual(self.inscripcion.estudiante.lugar_nacimiento, 'LAS MESAS', 'el lugar de nacimiento no coinciden')
        self.assertEqual(self.inscripcion.estudiante.estado_nacimiento, 'TACHIRA', 'estado de nacimiento no coinciden')
        self.assertEqual(self.inscripcion.estudiante.direccion_actual, 'CONJUNTO RESIDENCIAL MESA ALTA, CASA #19', 'la direccion actual no coinciden')
        self.assertEqual(self.inscripcion.estudiante.urbanizacion, 'LAS MESAS', 'la urbanizacion no coinciden')
        self.assertEqual(self.inscripcion.estudiante.localidad, 'LAS MESAS', 'la localidad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.estado, 'TACHIRA', 'el estado no coinciden')
        self.assertEqual(self.inscripcion.estudiante.email, 'alexandra@gmail.com', 'el email del estudiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.problema_fisico, 'NINGUNO', 'el problema fisico del estudiante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.deporte_practica, 'BOLAS CRIOLLAS', 'el deporte que practica no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.nombres, 'Darwel Alfonso', 'los nombres del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.apellidos, 'Quintero Duran', 'los apellidos del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.nacionalidad.letra, 'V', 'la nacionalidad del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.nacionalidad.descripcion, 'Venezolano', 'la descripcion de la nacionalidad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.cedula, '15686543', 'la cedula del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.empresa, 'BanfoAndes', 'la empresa del padre no coincide')
        self.assertEqual(self.inscripcion.estudiante.padre.cargo, 'Programador', 'el cargo del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.padre.email, 'darwel34@gmail.com', 'el email del padre no coincide')
        self.assertEqual(self.inscripcion.estudiante.padre.tel_tra, '0277-5410927', 'el telefono de trabajo del padre no coincide')
        self.assertEqual(self.inscripcion.estudiante.padre.tel_hab, '0277-5410938', 'el telefono de habitacion no coincide')
        self.assertEqual(self.inscripcion.estudiante.padre.tel_cel, '0414-5311345', 'el telefono celular del padre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.nombres, 'Ingrid Coromoto', 'los nombres de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.apellidos, 'Mora Guerrero', 'los apellidos de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.nacionalidad.letra, 'V', 'la nacionalidad de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.nacionalidad.descripcion, 'Venezolano', 'la descripcion de la nacionalidad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.cedula, '15686544', 'la cedula de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.empresa, 'Leche Tachira', 'la empresa de la madre no coincide')
        self.assertEqual(self.inscripcion.estudiante.madre.cargo, 'Programador', 'el cargo de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.madre.email, 'ingrid@gmail.com', 'el email de la madre no coincide')
        self.assertEqual(self.inscripcion.estudiante.madre.tel_tra, '0277-5410928', 'el telefono de trabajo de la madre no coincide')
        self.assertEqual(self.inscripcion.estudiante.madre.tel_hab, '0277-5410939', 'el telefono de habitacion no coincide')
        self.assertEqual(self.inscripcion.estudiante.madre.tel_cel, '0414-5311346', 'el telefono celular de la madre no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.nombres, 'Maria Juana', 'los nombres del representante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.apellidos, 'Garcia Peña', 'los apellidos del representante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.nacionalidad.letra, 'V', 'la nacionalidad del representante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.nacionalidad.descripcion, 'Venezolano', 'la descripcion de la nacionalidad no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.cedula, '15686548', 'la cedula del representante no coinciden')
        self.assertEqual(self.inscripcion.estudiante.representante.email, 'maria@gmail.com', 'el email del representante no coincide')
        self.assertEqual(self.inscripcion.estudiante.representante.tel_tra, '0277-5410930', 'el telefono de trabajo del representante no coincide')
        self.assertEqual(self.inscripcion.estudiante.representante.tel_hab, '0277-5410950', 'el telefono de habitacion del representante no coincide')
        self.assertEqual(self.inscripcion.estudiante.representante.tel_cel, '0414-5311349', 'el telefono celular del representante no coinciden')                 