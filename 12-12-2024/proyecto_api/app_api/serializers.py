from rest_framework import serializers
from app_api.models import  Producto, Categoria

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        #fields = "__all__"
        fields = ["codigo","descripcion","precio","stock", "categoria"]
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["cod_categoria","descripcion_categoria"]