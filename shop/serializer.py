from rest_framework.serializers import ModelSerializer

from .models import(
    ShopCategory,
    Shop,
    Connection,
)
from user_account.serializer import(
    UserSerializer
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
    category = ShopCategorySerializer(read_only=True)
    merchant = UserSerializer(read_only=True)
    
    class Meta:
        category_title = serializers.CharField()
        is_active = serializers.BooleanField(read_only=True)
        model = Shop
        fields = (
            "uuid",
            "title",
            "slug",
            "merchant",
            "title",
            "category",
            "is_active",
            #"connection",
        )

class ConnectionSerializer(ModelSerializer):
    sender = ShopSerializer()
    reciver = ShopSerializer()
    #connection = ShopSerializer()
    class Meta:
        model = Connection
        fields = (
            "uuid",
            "sender",
            "reciver"
        )



class BaseShopSerializer(serializers.Serializer):
    uuid = serializers.CharField()

