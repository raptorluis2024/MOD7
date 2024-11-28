from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medicamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.nombre
   
class Sucursal(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.RESTRICT)
    medicamento = models.ManyToManyField(Medicamento, through="Stock_Sucursal")
    
    def __str__(self):
        return f"{self.id}-{self.direccion}"

class Stock_Sucursal(models.Model):
    fecha_ingreso = models.DateField(auto_created=True)
    cantidad = models.IntegerField(null=False)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.RESTRICT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.RESTRICT)
    
    class Meta:
        # Restricción de unicidad
        unique_together = ('medicamento', 'sucursal')  
    
    def __str__(self):
        return f"{self.sucursal.direccion}-{self.medicamento.nombre}"
    
    
