from django.contrib import admin
from .models import Tarea,SubTarea

# Register your models here.
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion')
    list_display_links = ('id',)
    
@admin.register(SubTarea)
class SubTareaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','tarea')
    list_display_links = ('id',)


