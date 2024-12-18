# excel_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
path('cargar/', views.cargar_excel, name='cargar_excel'),
path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
path('exportar/csv/', views.exportar_csv, name='exportar_csv'),
path('exportar/json/', views.exportar_json, name='exportar_json'),

]