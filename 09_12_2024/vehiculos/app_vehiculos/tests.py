from django.test import TestCase
from app_vehiculos.services import crear_vehiculo
from app_vehiculos.services import crear_Chofer
from app_vehiculos.services import obtener_vehiculo
from app_vehiculos.services import creacion_registro_contable
from app_vehiculos.services import habilitar_chofer
from app_vehiculos.services import deshabilitar_chofer
from datetime import date
from app_vehiculos.services import asignar_vehiculo_a_chofer
from app_vehiculos.services import get_datos_choferes_vehiculos
#crear_vehiculo('xxx1','marca','nuevo',2020)
#print(obtener_vehiculo('xxx1'))
#crear_Chofer('2-2','Rodrigo','Vasquez',obtener_vehiculo('xxx1'))
#creacion_registro_contable(date.today(),obtener_vehiculo('xxx1'), 10000000)
# Create your tests here.
#habilitar_chofer("2-2")
#deshabilitar_chofer("1-1")
#signar_vehiculo_a_chofer("1-1",'xxx')


datos = get_datos_choferes_vehiculos()
for x in datos:
    print(x.rut, x.nombre, x.vehiculo_id.patente)