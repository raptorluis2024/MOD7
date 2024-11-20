from app1.models import Tarea,SubTarea

def mostrarAllTareas():
    tareas = Tarea.objects.all()
    return tareas

def getTarea(titulo=''):
    try:
        tarea = Tarea.objects.get(titulo= titulo)
        return tarea
    except Exception as ex:
        return None
    
def addTarea(titulo="", descripcion=""):
    
    tarea = Tarea(titulo=titulo, descripcion=descripcion)
    tarea.save()

def delTarea(titulo=""):
    
    Tarea.objects.filter(titulo=titulo).delete()

def crear_sub_tarea(id_tarea, descripcion):
    tarea = Tarea.objects.get(pk=id_tarea)
    subtarea = SubTarea(descripcion=descripcion, tarea=tarea, eliminada=False)
    subtarea.save()

def eliminar_sub_tarea(id_sub_tarea):
    sub_tarea = SubTarea.objects.get(pk=id_sub_tarea)
    sub_tarea.eliminada = True
    sub_tarea.save()

def getSubTareas():
    tareas = Tarea.objects.exclude(eliminada=True)
    lista=[]
    for tarea in tareas:
        subtareas = {"tarea":tarea,
                    "sub_tareas":tarea.subtarea_set.exclude(eliminada=True)}
        lista.append(subtareas)
    return lista

def imprimir_tareas(tareas=[]):
    for e in tareas:
        print("[{0}] - {1}".format(e['tarea'].id, e['tarea'].descripcion))
        
        for s in e['sub_tareas']:
            print("....[{0}] - {1}".format(s.id, s.descripcion))

    
    
    
    
    

