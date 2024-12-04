from django.forms import ModelForm
from gestion_inmueble.models import Inmueble

class formulario_inmueble(ModelForm):
    class Meta:
        model = Inmueble
        fields =['id_inmueble','nombre_inmueble']