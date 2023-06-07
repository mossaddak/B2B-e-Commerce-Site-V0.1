from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import(
    ShoppingCart
)


class ShoppingCartSerializer(ModelSerializer):

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
