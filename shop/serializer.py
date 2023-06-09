from rest_framework.serializers import ModelSerializer

from .models import(
    ShopCategory,
    Shop,
    Connection,
)

from rest_framework import serializers
class ShopCategorySerializer(ModelSerializer):

    class Meta:
        model = ShopCategory
        fields = (
            "uuid",
            "title",
            "slug"
        )

class ShopSerializer(ModelSerializer):
    #connection = ConnectionSerializer(many=True, read_only=True)
    category = ShopCategorySerializer(read_only=True)
    
    class Meta:
        category_title = serializers.CharField()
        is_active = serializers.BooleanField(read_only=True)
        model = Shop
        fields = (
            "_id",
            "title",
            "slug",
            "merchant",
            "title",
            "category",
            "is_active",
            "connection",
        )

class ConnectionSerializer(ModelSerializer):
    sender = ShopSerializer()
    reciver = ShopSerializer()
    class Meta:
        model = Connection
        fields = (
            "_id",
            "sender",
            "reciver"
        )



class BaseShopSerializer(serializers.Serializer):
    _id = serializers.CharField()

