import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","proyecto_inmueble.settings")
django.setup()
from .models import Region

select = "select * FROM gestion_inmueble_comuna WHERE region_id = 1"

query = Region.objects.raw(select)
for r in query:
    print(r)
    