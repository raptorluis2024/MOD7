from django.contrib import admin
from .models import Autor,AutorLibro,Libro

admin.site.register(Libro)
admin.site.register(AutorLibro)
admin.site.register(Autor)
# Register your models here.
