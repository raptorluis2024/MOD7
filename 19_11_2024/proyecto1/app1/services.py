from app1.models import Tarea

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
    
    

