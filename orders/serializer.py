from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import(
    OrderProduct
)
from shop.serializer import(
    ShopSerializer
)

class OrderSerializer(ModelSerializer):
    shop = ShopSerializer(read_only = True)
    class Meta:
        model = OrderProduct
        fields = (
            "_id",
            "shop",
            "cart_items",
            "status",
            "is_pay",

        )


# class ProductSerializer(ModelSerializer):
#     shop = ShopSerializer(read_only = True)
    
#     class Meta:
#         model = Product
#         fields = (
#             '_id',
#             'shop',
#             'title',
#             'slug',
#             'desc',
#             'price',
#             'img',
#         )
