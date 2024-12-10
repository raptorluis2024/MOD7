from django.shortcuts import render,loader,redirect
from django.http import HttpResponse
from app_vehiculos.services import get_datos_choferes_vehiculos, get_vehiculos
from app_vehiculos.forms import VehiculoForm

# Create your views here.

def index(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listado_choferes_vehiculos(request):
    template = loader.get_template('listado.html')
    listado = get_datos_choferes_vehiculos()
    context = {"listado":listado}
    return HttpResponse(template.render(context, request))

def formulario_vehiculo(request):   
    
    template = loader.get_template('formulariovehiculo.html')
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
        
def listadoVehiculos(request):
    template = loader.get_template('listadovehiculos.html')
    listado = get_vehiculos()
    context = {"listado":listado}
    return HttpResponse(template.render(context, request))

