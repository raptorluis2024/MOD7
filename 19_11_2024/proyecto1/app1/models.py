from django.db import models
# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, default="")
    descripcion = models.TextField(default="")
    fecha = models.DateTimeField(auto_now_add=True)
    eliminada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
class SubTarea(models.Model):
   
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion
    
