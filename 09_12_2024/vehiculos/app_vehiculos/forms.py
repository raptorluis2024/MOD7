from django.forms import ModelForm
from app_vehiculos.models import vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = vehiculo
        fields = ['patente','marca','modelo','year','activo']