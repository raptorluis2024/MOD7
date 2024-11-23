from registroconductores.models import Conductor, Vehiculo, Direccion
from datetime import date

def listarConductores():
    conductores = Conductor.objects.all()
    return conductores

def imprimir_modelos(): 
    conductores = Conductor.objects.all() 
    for c in conductores: 
        print(f"[{c.rut}]: {c.nombre} {c.apellido} - {c.fecha_nac}") 
        if hasattr(c, "direccion"): 
            d = c.direccion 
            print(f"dirección: {d.calle} {d.numero} / {d.comuna} / {d.ciudad} / {d.region}") 
        if hasattr(c, "vehiculo_set"): 
            vehiculos = c.vehiculo_set.all() 
            for v in vehiculos: print(f"Vehiculo: {v.marca} / {v.modelo} / {v.patente} / {v.year} ")

def crear_conductor(rut, nombre, apellido, fecha_nac): 
    if not rut.isdigit() and not isinstance(fecha_nac, date): 
        print("por favor validar los datos del conductor") 
        return 
    conductor = Conductor( rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac ) 
    conductor.save()
    
def obtener_conductor(rut): 
    try:
        return Conductor.objects.get(rut=rut)
    except Exception as ex:
        return  ex
    
def crear_direccion(conductor, calle, numero, dpto, comuna, ciudad, region): 
    direccion = Direccion( conductor=conductor, calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region ) 
    direccion.save()
    
def agregar_un_vehiculo(conductor, patente, marca, modelo, year): 
    vehiculo = Vehiculo( conductor=conductor, patente=patente, marca=marca, modelo=modelo, year=year ) 
    vehiculo.save()
    
def eliminar_vehiculo(vehiculo): 
    Vehiculo.objects.get(id=vehiculo.id).delete() 

def eliminar_conductor(conductor): 
    Conductor.objects.get(rut=conductor.rut).delete()
