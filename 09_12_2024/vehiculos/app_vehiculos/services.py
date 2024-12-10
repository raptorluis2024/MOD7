from app_vehiculos.models import Chofer, vehiculo, RegistroContabilidad

def crear_vehiculo(patente,marca,modelo,year):
    v=vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    v.save()
    
def crear_Chofer(rut,nombre, apellido, vehiculo):
    c=Chofer(rut=rut, nombre=nombre,apellido=apellido, vehiculo_id=vehiculo)
    c.save()
    
def obtener_vehiculo(patente):
    v=vehiculo.objects.get(patente=patente)
    return v

def habilitar_vehiculo(patente):
    v=obtener_vehiculo(patente=patente)
    v.activo=True
    v.save()

def deshabilitar_vehiculo(patente):
    v=obtener_vehiculo(patente=patente)
    v.activo=False
    v.save()

def creacion_registro_contable(fecha, vehiculo, valor):
    rc=RegistroContabilidad(vehiculo_id=vehiculo,fecha_compra=fecha, valor=valor)
    rc.save()
def deshabilitar_chofer(rut):
    c=obtener_chofer(rut)
    c.activo=False
    c.save()
def habilitar_chofer(rut):
    c=obtener_chofer(rut)
    c.activo=True
    c.save()
    
def obtener_chofer(rut):
    c=Chofer.objects.get(rut=rut)
    return c
    
def asignar_vehiculo_a_chofer(rut,patente):
    c=obtener_chofer(rut)
    v=obtener_vehiculo(patente=patente)
    c.vehiculo_id=v
    c.save()
    

