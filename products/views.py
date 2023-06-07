from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


from .models import(
    Product
)
from shop.models import(
    Shop
)
from .serializer import(
    ProductSerializer
)

# Create your views here.
class ProductView(APIView):
    def post(self, request):
        user = request.user
        
        try:
            shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        except Shop.DoesNotExist:
            raise ValidationError("Shop does not exist.")

        try:
            products = Product.objects.create(
                shop=shop,
                title=request.data['title'],
                desc=request.data['desc'],
                price=request.data['price'],
                img=request.data['img']
            )
        except KeyError:
            raise ValidationError("Invalid data. Required fields are missing.")
        
        serializer = ProductSerializer(products)

        return Response(
            {
                "data": serializer.data,
                "message": "Product successfully added"
            },
            status=status.HTTP_201_CREATED
        )
    
    def get(self, request):
        user = request.user
        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        data = Product.objects.filter(shop=shop)
        serializer = ProductSerializer(data, many=True)

        return Response(
            {
                "data":serializer.data,
                "message":"Data Fetch"
            }, status=status.HTTP_202_ACCEPTED
        )
        
