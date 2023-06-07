from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from shop.models import(
    Shop
)
from .models import (
    ShoppingCart
)
from products.models import(
    Product
)

class ShoppingCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user
        product_id = request.data['product_id']
        product = Product.objects.get(_id=product_id)

        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        
        is_product = ShoppingCart.objects.filter(shop=shop, product=product).first()
        print("Product ===============================>", product)
        print("Shop ===============================>", shop)
        #print("is_product================================>", is_product)

        if is_product:

            if is_product.quantity < 5:
                is_product.quantity += 1
                is_product.save()
                return Response(
                    {
                        "message": "Product cart updated"
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                    {
                        "message": "Already you added 5 item in a cart"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        else:
            
            ShoppingCart.objects.create(
                shop = shop,
                product = product,
                quantity = 1,
                totalPrice = product.price
            )
            return Response(
                {
                    "message": "New item added"
                },
                status=status.HTTP_201_CREATED
            )
