from django.test import TestCase
from app1.services import mostrarAllTareas,getTarea,addTarea,delTarea
# Create your tests here.
#print("hola mundo")

#print(mostrarAllTareas())
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


