from django.test import TestCase
from desafionew.models import DetalleSeccion
# Create your tests here.
print ("test")

lista = DetalleSeccion.objects.all()

for d in lista:
    print(d.estudiante, d.seccion.profesor, d.seccion)