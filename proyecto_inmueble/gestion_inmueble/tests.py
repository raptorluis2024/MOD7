from django.test import TestCase
import datetime as dt
from django.utils import timezone
from gestion_inmueble.services import listarComunas,getProfile, addUser
from gestion_inmueble.services import addRegion,delRegion, getComunas
from gestion_inmueble.services import obtener_comunas_por_region
from gestion_inmueble.services import getInmuebles
# Create your tests here.


now = timezone.now()
current_date = dt.date.today()
print(current_date, now)

#u = getProfile(rut='1-1')
#print(u.rut, u.direccion, u.user.username)
#print(addUser('test','test@123'))

print(listarComunas())
print("inmuebles****")
print(getInmuebles())

#print(addRegion(1,"ARICA"))
print(addRegion(2,"TARAPACA"))

#print(delRegion(2))

print(getComunas(1))

# Ejecutar la consulta y mostrar resultados
print("************************query raw *****************")
resultados = obtener_comunas_por_region(1)
print(resultados)
for resultado in resultados:
    print(resultado)


