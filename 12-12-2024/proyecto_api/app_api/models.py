from django.db import models

# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel 

# Create your models here.

class Categoria(SoftDeletableModel,models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    descripcion_categoria = models.CharField(max_length=50, null=False, blank=False)
     
    def __str__(self):
        return self.descripcion_categoria
    
class Producto(SoftDeletableModel,models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.codigo} {self.descripcion}"