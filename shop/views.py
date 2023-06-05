from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializer import (
    ShopCategorySerializer,
    ShopSerializer
)
from .models import(
    ShopCategory,
    Shop
)


# shop category======================================================
class ShopCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        if request.user.is_superuser:
            data = request.data
            try:
                serializer = ShopCategorySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "data": serializer.data,
                            "message": "Category Created"
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {
                            "errors": serializer.errors,
                            "message": "Invalid data"
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except Exception as e:
                print("Error====================", e)
                return Response(
                        {
                            "errors": {str(e)},
                            "message": "Invalid data"
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

        return Response(
            {
                "data": {},
                "message": "You don't have permissions for this action"
            },
            status=status.HTTP_403_FORBIDDEN
        )

    
    def get(self, request):
        data = ShopCategory.objects.all()
        serializer = ShopCategorySerializer(data, many=True)

        return Response(
            {
                "data":serializer.data,
                "message":"Data Fetch"
            }, status=status.HTTP_202_ACCEPTED
        )

class ShopCategoryDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def getCategory(self, slug):
        category = ShopCategory.objects.get(slug=slug)
        return category


    def get(self,request, slug):

        try:
            data = self.getCategory(slug)
            serializer = ShopCategorySerializer(data)
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
        if request.user.is_superuser:
            try:
                category = self.getCategory(slug)
                data = request.data
                serializer = ShopCategorySerializer(category, data=data, partial=True)
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
        if request.user.is_superuser:
            self.getCategory(slug).delete()

            return Response(
                {
                    "data": {},
                    "message": "Category successfully deleted"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        else:
            return Response(
                {
                    "data": {},
                    "message": "You don't have permissions for this action"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
#end========!

# shop ======================================================
class ShopView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            serializer = ShopSerializer(data=request.data)
            if serializer.is_valid():
                category_title = request.data['category_title']
                category = ShopCategory.objects.get(title=category_title)
                shop = Shop.objects.create(
                    merchant = request.user,
                    title = request.data['title'],
                    category = category,
                )
                last_shop = Shop.objects.last()
                shop_serializer = ShopSerializer(last_shop)
                return Response(
                    {
                        "data":shop_serializer.data,
                        "message":"Shop Successfully Created"
                    }, status=status.HTTP_201_CREATED
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

        except Exception as e:
            print("Error====================", e)
            return Response(
                    {
                        "errors": {str(e)},
                        "message": "Invalid data"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
    
    def get(self, request):
        data = Shop.objects.filter(merchant=request.user)
        
        serializer = ShopSerializer(data, many=True)

        return Response(
            {
                "data":serializer.data,
                "message":"Data Fetch"
            }, status=status.HTTP_202_ACCEPTED
        )

class ShopDetailsView(APIView):
    def getShop(self, slug):
        shop = Shop.objects.get(slug=slug)
        return shop
        
    def get(self,request, slug):

        try:
            shop = self.getShop(slug)
            merchant = shop.merchant
            user = request.user

            if user==merchant:
                data = self.getShop(slug)
                serializer = ShopSerializer(data)
                return Response(
                    {
                        "data":serializer.data,
                        "message":"Data Fetch"
                    },status=status.HTTP_202_ACCEPTED
                )
            else:
                return Response(
                    {
                        "data":{},
                        "message":"No data found"
                    },status=status.HTTP_204_NO_CONTENT
                )
                
        
        except Exception as e:
            return Response(
                {
                    "data":{},
                    "message":"Something wrong"
                },status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def put(self, request, slug):
        try:
            shop = self.getShop(slug)
            merchant = shop.merchant
            user = request.user

            if merchant == user:
                data = request.data
                serializer = ShopSerializer(shop, data=data, partial=True)
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
            else:

                return Response(
                    {
                        "data":{},
                        "message":"No Shop Found"
                    },status=status.HTTP_204_NO_CONTENT
                )

            
        except Exception as e:
            return Response(
                {
                    "data":{},
                    "message":"Something wrong"
                },status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def delete(self, request, slug):
        
        shop = self.getShop(slug)
        merchant = shop.merchant
        user = request.user

        if merchant == user:
            shop.delete()

            return Response(
                {
                    "data": {},
                    "message": "Shop successfully deleted"
                },
                status=status.HTTP_202_ACCEPTED
            )
        
        else:
            return Response(
                {
                    "data": {},
                    "message": "No Data Found"
                },
                status=status.HTTP_204_NO_CONTENT
            )
#end========!

# activate shop ======================================================
class ActivateShopView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            _id = request.data["_id"]
            user = request.user

            # Deactivate all other shops for the user
            Shop.objects.filter(merchant=user).update(is_active=False)
            shop = Shop.objects.get(_id=_id, merchant = user)
            print("shop====================================>", shop)
            shop.is_active = True
            shop.save()
            return Response({"message": "Shop activated successfully."}, status=status.HTTP_200_OK)      

        except Exception as e:
            print("Error====================", e)
            return Response(
                {
                    "errors": {str(e)},
                    "message": "Invalid data"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
#end========!


