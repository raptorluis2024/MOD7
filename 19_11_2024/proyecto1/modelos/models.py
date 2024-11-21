from django.db import models

# Create your models here.

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    edad = models.IntegerField(null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualización = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.cliente_id}-{self.nombre}-{self.apellido}"
    
class Direccion(models.Model):
    cliente = models.OneToOneField( Cliente,blank=False,null=False,on_delete=models.CASCADE)
    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.calle
    
    
    