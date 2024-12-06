from django.forms import ModelForm
from gestion_inmueble.models import Inmueble, Profile

class formulario_inmueble(ModelForm):
    class Meta:
        model = Inmueble
        fields =['id_inmueble','nombre_inmueble']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['rut','direccion','telefono','correo','id_tipo_user' ]


