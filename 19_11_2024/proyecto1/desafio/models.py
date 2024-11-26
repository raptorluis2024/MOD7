from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField("Curso", related_name="estudiantes")
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.OneToOneField(
    "Estudiante", related_name="direccion", on_delete=models.CASCADE
    )
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField("Curso", related_name="profesores")