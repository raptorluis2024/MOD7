from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.rut} {self.nombre} {self.apellido}"
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.OneToOneField(
    "Estudiante", related_name="AlumnoDireccion", on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.calle} {self.numero}"
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField("Curso", through="Seccion")
    
    def __str__(self):
        return f"{self.rut} {self.nombre} {self.apellido}"
    
class Seccion(models.Model):
    id = models.IntegerField(primary_key=True)
    curso = models.ForeignKey(Curso, related_name="CursoSeccion", on_delete=models.CASCADE)
    profesor = models.ForeignKey("Profesor", on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return f"Seccion {self.id} Curso {self.curso.nombre}"
    
    class Meta:
        # Restricción de unicidad
        unique_together = ('curso', 'profesor', 'id')
    
class DetalleSeccion(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, related_name="alumnoseccion", on_delete=models.CASCADE)
    fecha_alta = models.DateField()
    
    def __str__(self):
        return f"Seccion {self.seccion} Estudiante {self.estudiante}"
        
    class Meta:
        # Restricción de unicidad
        unique_together = ('seccion', 'estudiante')
        
    
    
    