from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializer import (
    ShopCategorySerializer
)
from .models import(
    ShopCategory
)



# Create your views here.
class ShopCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        if request.user.is_superuser:
            data = request.data
            serializer = ShopCategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "data":serializer.data,
                        "message":"Category Created"
                    }, status=status.HTTP_201_CREATED
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        return Response(
            {
                "data":{},
                "message":"You don't have permissions for this action"
            },status=status.HTTP_400_BAD_REQUEST
            
        )
    
    def get(self, request):
        
        if request.user.is_superuser:
            data = ShopCategory.objects.all()
            serializer = ShopCategorySerializer(data, many=True)

            return Response(
                {
                    "data":serializer.data,
                    "message":"Data Fetch"
                }, status=status.HTTP_202_ACCEPTED
            )
    
        return Response(
            {
                "data":{},
                "message":"You don't have permissions for this action"
            },status=status.HTTP_400_BAD_REQUEST
        )
    

class ShopCategoryDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def getCategory(self, _id):
        category = ShopCategory.objects.get(_id=_id)
        return category


    def get(self,request, _id):
        if request.user.is_superuser:

            try:
                data = self.getCategory(_id)
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
        else:
            return Response(
                {
                    "data":{},
                    "message":"You don't have permissions for this action"
                },status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, _id):
        if request.user.is_superuser:

            try:
                category = self.getCategory(_id)
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
        
    
    def delete(self, request, _id):
        if request.user.is_superuser:
            self.getCategory(_id).delete()

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

