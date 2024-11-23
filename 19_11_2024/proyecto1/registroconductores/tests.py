from django.test import TestCase

from registroconductores.services import listarConductores
from registroconductores.services import crear_conductor
from registroconductores.services import obtener_conductor
from registroconductores.services import crear_direccion
from registroconductores.services import agregar_un_vehiculo
from registroconductores.services import imprimir_modelos

#for c in listarConductores():
#    print(c)
"""    
crear_conductor("11111","qaaaaaaa","asadasdasd","2024-11-11")
for c in listarConductores():
    print(c)
"""
# Create your tests here.
#c =  obtener_conductor("11111")
#print("datos del coductor ",c)

#crear_direccion(c,"calle 1","1111","12","aaaa","aaaaa","12")
#agregar_un_vehiculo(c,"ttttt","marca","new","2010-11-11")

imprimir_modelos()