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
from .serilizer import (
    ShoppingCartSerializer
)

from drf_spectacular.utils import extend_schema

class ShoppingCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    @extend_schema(
        request=ShoppingCartSerializer,
        responses={201: ShoppingCartSerializer},
    )
    def post(self, request):
        user = request.user
        uuid = request.data['uuid']

        try:
            product = Product.objects.get(uuid=uuid)
        except Exception as e:
            return Response(
                {
                    "message":str(e),
                }
                
            )
        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        is_product = ShoppingCart.objects.filter(shop=shop, product=product).first()
        print("Product ===============================>", product)
        print("Shop ===============================>", shop)

        if is_product:

            if is_product.quantity < 5:
                is_product.quantity += 1
                is_product.totalPrice = product.price * is_product.quantity
                is_product.save()
                return Response(
                    {
                        "message": "Product cart updated"
                    },
                    status=status.HTTP_201_CREATED
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


class MyCartView(APIView):

    @extend_schema(
        request=ShoppingCartSerializer,
        responses={200: ShoppingCartSerializer},
    )

    def get(self, request):
        user = request.user

        try:
            shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        except Exception as e:
            return Response(
                {
                    "message": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

              
        data = ShoppingCart.objects.filter(shop=shop)
        serializer = ShoppingCartSerializer(data, many=True)

        return Response(
            {
                "data":serializer.data
            },status=status.HTTP_200_OK
        )

        
