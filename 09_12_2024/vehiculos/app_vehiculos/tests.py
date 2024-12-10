from django.test import TestCase
from app_vehiculos.services import crear_vehiculo
from app_vehiculos.services import crear_Chofer
from app_vehiculos.services import obtener_vehiculo
from app_vehiculos.services import creacion_registro_contable
from app_vehiculos.services import habilitar_chofer
from app_vehiculos.services import deshabilitar_chofer
from datetime import date
from app_vehiculos.services import asignar_vehiculo_a_chofer
#crear_vehiculo('xxx1','marca','nuevo',2020)
print(obtener_vehiculo('xxx1'))
#crear_Chofer('2-2','Rodrigo','Vasquez',obtener_vehiculo('xxx1'))
#creacion_registro_contable(date.today(),obtener_vehiculo('xxx1'), 10000000)
# Create your tests here.
habilitar_chofer("2-2")
deshabilitar_chofer("1-1")
asignar_vehiculo_a_chofer("1-1",'xxx')
