from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=40, null=False, blank=False)
    
    def __str__(self):
        return f"{self.id_region}-{self.nombre_region}"
    
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=40, null=False, blank=False)
    region = models.ForeignKey(Region, related_name="comunaregion", on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('id_comuna', 'region')
    
    def __str__(self):
        return f"{self.id_comuna}-{self.nombre_comuna}"
    
class Tipo_Usuario(models.Model):
    codigo_tipo_usuario = models.IntegerField(primary_key=True)
    tipo_user = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f"{self.codigo_tipo_usuario}-{self.tipo_user}"

class Tipo_inmueble(models.Model):
    codigo_tipo_inmueble = models.IntegerField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"{self.codigo_tipo_inmueble}-{self.tipo_inmueble}"
   
class Profile(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    direccion = models.CharField(max_length=50, null=False, blank= False)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_tipo_user = models.ForeignKey(Tipo_Usuario,on_delete=models.CASCADE,null=True,)
    
    def __str__(self):
        return self.rut
 
class Inmueble(models.Model):
    id_inmueble = models.IntegerField(primary_key=True)
    nombre_inmueble = models.TextField()
    descripcion = models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_banos = models.IntegerField(default =1, null=False, blank=False)
    numero_hab = models.IntegerField(default =1)
    direccion = models.CharField(max_length=200)
    id_user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,)
    id_tipo_inmueble = models.ForeignKey(Tipo_inmueble,on_delete=models.CASCADE,null=True,)
    id_comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,)
    
    def __str__(self):
        return f"{self.id_inmueble}-{self.nombre_inmueble}"


    
    

    
    

    
    