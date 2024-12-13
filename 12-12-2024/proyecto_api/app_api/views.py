from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,loader,redirect
from django.contrib.auth.forms import AuthenticationForm,authenticate
from django.contrib.auth import login,logout
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from app_api.serializers import ProductoSerializer, CategoriaSerializer
from app_api.models import Producto, Categoria
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.


@login_required
def index(request):
    return render (request, "index.html",{})

def loginPage(request):

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
            template = loader.get_template('index.html')
            return HttpResponse(template.render(context, request))
        
def logout_(request):
    logout(request)
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


######### 

class Producto_APIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        producto = Producto.objects.all()
        serializer =  ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Producto_APIView_Detail(APIView):
    def get_objetc(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        producto = self.get_objetc(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self, request, pk, Format=None):
         producto = self.get_objetc(pk)
         serializer = ProductoSerializer(producto, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        producto = self.get_objetc(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################ API para las Categorias ###################
class Categoria_APIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        categoria = Categoria.objects.all()
        serializer =  CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Categoria_APIView_Detail(APIView):
    def get_objetc(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        categoria = self.get_objetc(pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, pk, Format=None):
         categoria = self.get_objetc(pk)
         serializer = CategoriaSerializer(categoria, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        categoria = self.get_objetc(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
#########  Autenticación #################

class LoginAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email}
        )