from django.urls import path
from app_api.views import *


app_name='app_api'

urlpatterns = [
    path('api/producto/', Producto_APIView.as_view()),
    path('api/producto/<int:pk>/',Producto_APIView_Detail.as_view()),
    path('api/categoria/', Categoria_APIView.as_view()),
    path('api/categoria/<int:pk>/',Categoria_APIView_Detail.as_view()),
      
]