from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import(
    ShoppingCart
)
from shop.serializer import (
    ShopSerializer
)
from products.serializer import(
    ProductSerializer
)

class ShoppingCartSerializer(ModelSerializer):
   shop = ShopSerializer(read_only=True)
   product = ProductSerializer(read_only=True)

   class Meta:
        product_id = serializers.CharField()
        model = ShoppingCart
        fields = (
            "_id",
            "shop",
            "product",
            "quantity",
            "totalPrice"
        )

   

