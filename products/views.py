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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
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
    
    
class MyProductView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

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

class AllProductView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=user))
        shopCategory = shop.category
        print("Shop category==================================>", shopCategory)
        data = Product.objects.filter(shop__category=shopCategory)
        print("Category Product==============================", data)
        serializer = ProductSerializer(data, many=True)

        return Response(
            {
                "data":serializer.data,
                "message":"Data Fetch"
            }, status=status.HTTP_202_ACCEPTED
        )

class ProductDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def getProduct(self, slug):
        product = Product.objects.get(slug=slug)
        print("Product===================================================", product)
        return product
    
    def get(self,request, slug):

        try:
            data = self.getProduct(slug)
            print("Product==============================>", data)
            serializer = ProductSerializer(data)
            return Response(
                {
                    "data":serializer.data,
                    "message":"Data Fetch"
                },status=status.HTTP_202_ACCEPTED
            )
        
        except Exception as e:
            return Response(
                {
                    "data":{},
                    "message":"Something wrong"
                },status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, slug):

        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=request.user))
        if shop:
            try:
                product = self.getProduct(slug)
                data = request.data
                serializer = ProductSerializer(product, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "data": serializer.data,
                            "message": "Category Updated"
                        },
                        status=status.HTTP_202_ACCEPTED
                    )
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                return Response(
                    {
                        "data":{},
                        "message":"Something wrong"
                    },status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {
                    "data": {},
                    "message": "You don't have permissions for this action"
                },
                status=status.HTTP_202_ACCEPTED
            )
        
    def delete(self, request, slug):
        shop = Shop.objects.get(Q(is_active=True) & Q(merchant=request.user))

        if shop:
            self.getProduct(slug).delete()

            return Response(
                {
                    "data": {},
                    "message": "Product successfully deleted"
                },
                status=status.HTTP_200_OK
            )
        
        else:
            return Response(
                {
                    "data": {},
                    "message": "You don't have permissions for this action"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


