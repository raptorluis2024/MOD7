from django.test import TestCase
#from desafionew.models import DetalleSeccion
from desafionew.services import listarEstudiantes,listadoSecciones
from desafionew.services import crearCurso,listarCursos
from desafionew.services import crearProfesor

# Create your tests here.

#lista = DetalleSeccion.objects.all()

#for d in lista:
#    print(d.estudiante, d.seccion.profesor, d.seccion)
"""
lista = listarEstudiantes()
print(lista["titulo"])
for e in lista["estudiantes"]:
    print(e)
"""
lista = listadoSecciones()
for l in lista:
    print(l["estudiantes"])
    

#print(crearCurso(111,"CURSO TEST1", 1))
#for c in listarCursos():
#    print(c)
#print(crearProfesor(2222,"bbbbb","bbbbbb",True,"LPH"))
