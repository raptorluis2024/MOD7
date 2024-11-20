from django.test import TestCase
from app1.services import mostrarAllTareas,getTarea,addTarea,delTarea
from app1.services import  getSubTareas,imprimir_tareas,crear_sub_tarea
from app1.services import eliminar_sub_tarea

# Create your tests here.
#print("hola mundo")

#print(mostrarAllTareas())
def paso():
        
    for t in mostrarAllTareas():
        print(f"{t.id} {t.titulo} {t.descripcion} {t.fecha}")

    t = getTarea(input("ingrese la tarea a buscar : "))
    if t is not None:
        print(t)
    else:
        print("no hay tarea")
        
    t = input("Ingrese nombre de la tarea")
    d = input("Ingrese la descripcion de la tarea")
    addTarea(t,d)

    t = input("Ingrese nombre de la tarea a eliminar  ")
    delTarea(t)


tareas = getSubTareas()
imprimir_tareas(tareas)
crear_sub_tarea(2,"SUB TAREA 233 TAREA 2")
tareas = getSubTareas()
imprimir_tareas(tareas)
eliminar_sub_tarea(2)
tareas = getSubTareas()
imprimir_tareas(tareas)
delTarea("TAREA 2")
tareas = getSubTareas()
imprimir_tareas(tareas)