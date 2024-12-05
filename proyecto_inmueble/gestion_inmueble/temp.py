import sys
from pathlib import Path
import os
import django
sys.path.append(Path(__file__).resolve().parent.parent.__str__())
os.environ.setdefault("DJANGO_SETTINGS_MODULE","proyecto_inmueble.settings")
django.setup()
from gestion_inmueble.models import Comuna, Inmueble

def getComunas(id_region):
    select = f"""
    select * FROM gestion_inmueble_comuna 
    WHERE region_id = {id_region}
    """

    query = Comuna.objects.raw(select)
    print(query)
    for r in query:
        print(r, type(r))

def getInmuebles(comuna):
    consulta = f"""
    SELECT gii.id_inmueble, gii.nombre_inmueble,
    gic.nombre_comuna, gir.nombre_region 
    FROM public.gestion_inmueble_inmueble gii 
    inner join public.gestion_inmueble_comuna gic 
    on gii.id_comuna_id = gic.id_comuna 
    inner join public.gestion_inmueble_region gir 
    on gic.region_id = gir.id_region 
    where gic.nombre_comuna like '%{comuna}%'
    """
    
    print(consulta)
    query = Inmueble.objects.raw(consulta)
    print(query)
    for i in query:
        print(i)
        
getComunas(13)
getInmuebles('MAI')
    