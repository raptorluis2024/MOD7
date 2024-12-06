from django.shortcuts import render,loader,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gestion_inmueble.models import Inmueble, Profile
from gestion_inmueble.services import getInmuebles
from django.shortcuts import get_object_or_404
from gestion_inmueble.forms import formulario_inmueble, ProfileForm


# Create your views here.

@login_required      
def inmuebles(request):
    user = request.user
    profile = get_object_or_404(Profile, user = user) 
    template = loader.get_template('inmuebles.html')
    inmuebles = Inmueble.objects.all()
    context = {'inmuebles': inmuebles, "profile":profile}
    return HttpResponse(template.render(context, request))

@login_required  
def crear_inmueble(request):
    template = loader.get_template('crear_inmueble.html')
    context = {'form':formulario_inmueble}
    return HttpResponse(template.render(context, request))

def sign_out(request):
    logout(request)
    return redirect('home')


def sign_up(request):
    template = loader.get_template('sign_up.html')
    if request.method == "GET":
        context = {'form': UserCreationForm}
        return HttpResponse(template.render(context, request))
    else:
        if request.POST["password1"] == request.POST["password2"]:
            usuario = request.POST["username"]
            clave = request.POST["password1"]
            try:
                user = User.objects.create_user(username=usuario, password=clave)
                user.save()
                users = User.objects.all()
                login(request,user)
                template = loader.get_template('inmuebles.html')
                context = {'inmuebles': getInmuebles()}
                return HttpResponse(template.render(context, request))
               
            except Exception as ex:
                context={"error":ex,'form': UserCreationForm}
                return HttpResponse(template.render(context, request))
        else:
            context={"error":"Las contraseñas no coinciden",'form': UserCreationForm}
            return HttpResponse(template.render(context, request))
        
def log_in(request):
    template = loader.get_template('login.html')
    context = {'form':AuthenticationForm}
    if request.method == "GET":
        return HttpResponse(template.render(context, request))
    else:
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate( request, username=usuario, password=clave)
        if user is None:
            context["error"] = "Usuario o contraseña incorrectos"
            return HttpResponse(template.render(context, request))
        else:
               
                login(request, user)
                template = loader.get_template('inmuebles.html')
                inmuebles = getInmuebles()
                usuario = User.objects.filter(username=usuario).values()[0]["username"]
                user = get_object_or_404(User, username = request.user) 
                profile = get_object_or_404(Profile, user = user) 
                context = {"usuario_logueado":usuario, "inmuebles":inmuebles, "profile":profile}
                return HttpResponse(template.render(context, request))
                
@login_required                
def profileUpdate(request):
    template = loader.get_template('profile.html')
    
    if request.method == "GET":
        try:
            perfil = get_object_or_404(Profile, user=request.user)
            form = ProfileForm(instance=perfil)
            context = {'form':form}
            return HttpResponse(template.render(context, request))
        except Exception as ex:
            form = ProfileForm()
            context = {'form':form}
            return HttpResponse(template.render(context, request))
            
    else:
        return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))


