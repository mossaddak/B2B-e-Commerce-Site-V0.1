from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import(
    Product
)
from shop.serializer import(
    ShopSerializer
)

class ProductSerializer(ModelSerializer):
    shop = ShopSerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = (
            'uuid',
            'shop',
            'title',
            'slug',
            'desc',
            'price',
            'img',
        )
