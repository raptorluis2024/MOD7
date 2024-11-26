from django.test import TestCase
#from desafionew.models import DetalleSeccion
from desafionew.services import listarEstudiantes,listadoSecciones

# Create your tests here.

#lista = DetalleSeccion.objects.all()

#for d in lista:
#    print(d.estudiante, d.seccion.profesor, d.seccion)

lista = listarEstudiantes()
print(lista["titulo"])
for e in lista["estudiantes"]:
    print(e)

lista = listadoSecciones()
for l in lista:
    print(l)
