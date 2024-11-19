from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    
class Ejemplo(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=50)