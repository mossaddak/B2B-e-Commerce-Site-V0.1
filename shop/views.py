from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializer import (
    ShopCategorySerializer
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
