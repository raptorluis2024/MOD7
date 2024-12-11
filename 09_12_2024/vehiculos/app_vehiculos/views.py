from django.shortcuts import render,loader, redirect
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from app_vehiculos.services import get_datos_choferes_vehiculos
from app_vehiculos.services import get_vehiculos
from app_vehiculos.forms import VehiculoForm
# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def listado(request):
    template = loader.get_template("listado.html")
    lista = get_datos_choferes_vehiculos()
    context = {"lista":lista}
    return HttpResponse(template.render(context, request))

def listado_vehiculos(request):
    template = loader.get_template("listado_vehiculos.html")
    lista = get_vehiculos()
    context = {"lista":lista}
    return HttpResponse(template.render(context, request))

def formulario_vehiculo(request):
    template = loader.get_template("formulariovehiculo.html")
    if request.method == "GET":
        context = {"form":VehiculoForm}
        return HttpResponse(template.render(context, request))
    else:
        try:
            v = VehiculoForm(request.POST)
            if v.is_valid():
                v.save()
                template = loader.get_template('formulariovehiculo.html')
                context={"error":"Vehiculo creado satisfactoriamente","form":VehiculoForm}
                return HttpResponse(template.render(context, request))
            else:
                context={"error":"Error al procesar el formulario","form":VehiculoForm}
                return HttpResponse(template.render(context, request))
        except Exception as ex:
            context={"error":ex,'form': VehiculoForm}
            return HttpResponse(template.render(context, request))
            
                
            

    
    
