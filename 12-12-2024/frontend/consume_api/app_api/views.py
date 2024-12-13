from django.shortcuts import render,loader
from django.http import HttpResponse
import requests
import json

headers = {'Authorization':'Token 833b46505b0f1ad6441f0428668dcbd65c1d416b'}
def getData():
    url = "http://127.0.0.1:8000/api/producto/"
    datos = requests.get(url, headers=headers)
    elementos = datos.json()
    return elementos

# Create your views here.
def index(request):
    return render (request, "index.html",{})

def listar(request):
    template = loader.get_template('listar.html')
    context = {'lista':getData()}
    return HttpResponse(template.render(context, request))
