from rest_framework.serializers import ModelSerializer

from .models import(
    ShopCategory
)

class ShopCategorySerializer(ModelSerializer):

    class Meta:
        model = ShopCategory
        fields = (
            "_id",
            "title"
        )

