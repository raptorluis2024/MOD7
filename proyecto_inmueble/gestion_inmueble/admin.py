from django.contrib import admin
from gestion_inmueble.models import Comuna, Region, Inmueble
from gestion_inmueble.models import Profile,Tipo_inmueble,Tipo_Usuario

# Register your models here.
@admin.register(Tipo_Usuario)
class Tipo_UsuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo_tipo_usuario','tipo_user')
    list_display_links = ('codigo_tipo_usuario',)
    
@admin.register(Tipo_inmueble)
class Tipo_inmuebleAdmin(admin.ModelAdmin):
    list_display = ('codigo_tipo_inmueble','tipo_inmueble')
    list_display_links = ('codigo_tipo_inmueble',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('rut','direccion', 'telefono')
    list_display_links = ('rut',)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id_inmueble','nombre_inmueble', 'descripcion')
    list_display_links = ('id_inmueble',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region','nombre_region')
    list_display_links = ('id_region',)
    
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id_comuna','nombre_comuna', 'region')
    list_display_links = ('id_comuna','region')
    

