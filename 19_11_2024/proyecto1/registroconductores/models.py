from django.db import models

# Create your models here.
class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    conductor = models.OneToOneField("Conductor", null=False, blank=False
    ,on_delete=models.CASCADE)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    year = models.DateField(null=False, blank=False)
    conductor = models.ForeignKey("Conductor", null=False, blank=False,
    on_delete=models.CASCADE)