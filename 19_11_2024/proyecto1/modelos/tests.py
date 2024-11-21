from django.test import TestCase

# Create your tests here.
from .models import Cliente, Direccion
cliente = Cliente(nombre="Juan", apellido="Perez", edad=30)
cliente.save() 
direccion = Direccion(cliente=cliente, calle="alguna calle", numero="1234", dpto="1234",
comuna="Santiago", ciudad="Santiago")
direccion.save()