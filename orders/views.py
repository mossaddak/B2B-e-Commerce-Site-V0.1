from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
import json
from django.db.models import Sum

from cart.models import(
    ShoppingCart
)
from shop.models import(
    Shop
)
from .models import(
    OrderProduct
)
from .models import(
    ProductStatus
)
from .serializer import(
    OrderSerializer
)

class OrderProductView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            shop = Shop.objects.get(is_active=True, merchant=request.user)
        except Shop.DoesNotExist:
            return Response(
                {
                    "message": "Shop not found or inactive.",
                    "date": ""
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cart_products = ShoppingCart.objects.filter(shop=shop)
        print("Cart Product===================================>", cart_products)

        total_price = 0
        order_items = []
        for product in cart_products:
            item = {
                "product_name": product.product.title,
                "product_id": product.product.uuid,
                "quantity": product.quantity,
                "total_price": product.totalPrice
            }
            total_price += (product.quantity * product.totalPrice)
            order_items.append(item)
        total_quantity = cart_products.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_price = cart_products.aggregate(total_price=Sum('totalPrice'))['total_price']

        if not len(order_items)<1:
            order_product = OrderProduct.objects.create(
                shop=shop,
                cart_items=str(order_items),
                total_qty=total_quantity,
                total_price=total_price
            )
            cart_products.delete()
            serializer = OrderSerializer(order_product)
            return Response(
                {
                    "data":serializer.data,
                    "message": "Order placed successfully."
                },
                status=status.HTTP_201_CREATED
            )
        else:
             return Response(
                {
                    "data":{},
                    "message": "You don't have any item in cart"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class MyOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        shop = Shop.objects.get(is_active=True, merchant=request.user)
        data = OrderProduct.objects.filter(shop=shop)
        serializer = OrderSerializer(data, many=True)


        return Response(
            {
                "data":serializer.data,
                "message": "data fetch"
            },
            status=status.HTTP_200_OK
        )


