from django.contrib import admin
from gestion_inmueble.models import Comuna, Region
# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region','nombre_region')
    list_display_links = ('id_region',)
    
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id_comuna','nombre_comuna', 'region')
    list_display_links = ('id_comuna','region')
    

