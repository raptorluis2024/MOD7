import sys
from pathlib import Path
import os
import django
sys.path.append(Path(__file__).resolve().parent.parent.__str__())
os.environ.setdefault("DJANGO_SETTINGS_MODULE","proyecto_inmueble.settings")
django.setup()
from gestion_inmueble.models import Comuna, Inmueble, Region

def getComunas(id_region):
    select = f"""
    select * FROM gestion_inmueble_comuna 
    WHERE region_id = {id_region}
    """

    query = Comuna.objects.raw(select)
    print(query, "total de filas ", len(query), type(query))
    for r in query:
        print(r, type(r))

def getInmuebles_raw(comuna):
    consulta = f"""SELECT gii.id_inmueble, gii.nombre_inmueble,gic.nombre_comuna, gir.nombre_region
    FROM public.gestion_inmueble_inmueble gii 
    inner join public.gestion_inmueble_comuna gic 
    on gii.id_comuna_id = gic.id_comuna 
    inner join public.gestion_inmueble_region gir 
    on gic.region_id = gir.id_region 
    where gic.nombre_comuna  like %s 
    """
    params = ['%' + comuna + '%']
    resultado = Inmueble.objects.raw(consulta,params)
    for i in resultado:
        print(i.id_inmueble, i.nombre_inmueble, i.nombre_comuna, i.nombre_region)
     
    archi1=open("../inmuebles1.txt","w")
    for r in resultado:
        archi1.write(str(r.id_inmueble) + ',' 
                     + r.nombre_inmueble + ',' 
                     + r.nombre_comuna + ',' 
                     + r.nombre_region)
        archi1.write("\n")
    archi1.close()
        
def get_list_inmuebles(name,descr):
    lista_inmuebles = Inmueble.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=descr)
    
    archi1=open("../inmuebles2.txt","w")
    for l in lista_inmuebles:
        archi1.write(str(l))
        archi1.write("\n")
    archi1.close()
    
def get_list_inmuebles_comuna():
    comunas = [x.id_comuna for x in Comuna.objects.all()]
    for c in comunas:
        print(c)
        try:
            lista_inmuebles = Inmueble.objects.filter(id_comuna=c)
            archi1=open("../all_inmbuebles.txt","a")
            for l in lista_inmuebles:
                archi1.write(str(l))
                archi1.write(',')
                archi1.write(str(c))
                archi1.write("\n")
            archi1.close()
        except Exception:
            pass

#getComunas(13)
#getInmuebles_raw('M')
#get_list_inmuebles('tes','des')
get_list_inmuebles_comuna()




    