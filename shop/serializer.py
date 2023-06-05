from rest_framework.serializers import ModelSerializer

from .models import(
    ShopCategory,
    Shop

)

class ShopCategorySerializer(ModelSerializer):

    class Meta:
        model = ShopCategory
        fields = (
            "_id",
            "title",
        )

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

