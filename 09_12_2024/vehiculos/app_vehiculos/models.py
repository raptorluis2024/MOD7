from django.db import models

# Create your models here.
class vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=20, null=False)
    year = models.IntegerField(null=False)
    def __str__(self):
        return self.patente 
        
class Chofer(models.Model):
    rut = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    vehiculo_id = models.OneToOneField(vehiculo,related_name="ChoferVehiculo",on_delete=models.RESTRICT)
    def __str__(self):
        return self.rut
    
    
class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(null=False)
    vehiculo_id = models.OneToOneField(vehiculo,related_name= "RegistroVehiculo",on_delete=models.RESTRICT)
    def __str__(self):
        return str(self.id)
    
    