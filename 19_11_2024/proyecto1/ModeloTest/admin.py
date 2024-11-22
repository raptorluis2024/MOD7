from django.contrib import admin
from .models import Medicamento, Sucursal, Comuna, Stock_Sucursal

# Register your models here.
admin.site.register(Medicamento)
admin.site.register(Sucursal)
admin.site.register(Comuna)
admin.site.register(Stock_Sucursal)