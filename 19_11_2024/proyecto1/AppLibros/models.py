from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    libros = models.ManyToManyField(Libro, related_name="autores")
    
    def __str__(self):
        return self.nombre
    
class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creado_por = models.CharField(max_length=50, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.autor.nombre}-{self.libro.titulo}"