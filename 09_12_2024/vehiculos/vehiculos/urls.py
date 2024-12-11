"""
URL configuration for vehiculos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_vehiculos.views import index
from app_vehiculos.views import listado
from app_vehiculos.views import listado_vehiculos
from app_vehiculos.views import formulario_vehiculo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('listado/',listado,name="listado"),
    path('listado_vehiculos/',listado_vehiculos,name="listado_vehiculos"),
    path('formulario_vehiculo/',formulario_vehiculo,name="formulario"),
]
