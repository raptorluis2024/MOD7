from app_vehiculos.models import Chofer, vehiculo

def crear_vehiculo(patente,marca,modelo,year):
    v=vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    v.save()
    

