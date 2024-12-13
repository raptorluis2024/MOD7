from django.test import TestCase

# Create your tests here.

import requests

headers = {'Authorization':'Token 833b46505b0f1ad6441f0428668dcbd65c1d416b'}
def getData():
    url = "http://127.0.0.1:8000/api/producto/"
    datos = requests.get(url, headers=headers)
    print(datos)
    elementos = datos.json()
    return elementos

for x in getData():
    print(x, type(x), x['codigo'])