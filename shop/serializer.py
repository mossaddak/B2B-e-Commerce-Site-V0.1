from rest_framework.serializers import ModelSerializer

from .models import(
    ShopCategory,
    Shop,
    Connection
)

from user_account.serializer import(
    UserSerializer
)
from rest_framework import serializers


class ShopCategorySerializer(ModelSerializer):

    class Meta:
        model = ShopCategory
        fields = (
            "_id",
            "title",
            "slug"
        )

class ConnectionSerializer(ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"

class ShopSerializer(ModelSerializer):
    connection = ConnectionSerializer(many=True, read_only=True)
    merchant = UserSerializer(read_only=True)
    category = ShopCategorySerializer(read_only=True)
    
    class Meta:
        category_title = serializers.CharField()
        is_active = serializers.BooleanField(read_only=True)
        model = Shop
        fields = (
            "_id",
            "title",
            "merchant",
            "title",
            "category",
            "is_active",
            "connection"
        )

