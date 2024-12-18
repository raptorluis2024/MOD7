# excel_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
path('cargar/', views.cargar_excel, name='cargar_excel'),
path('exportar/', views.exportar_excel, name='exportar_excel'),

]