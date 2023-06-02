from django.contrib import admin
from django.urls import path, include
from .views import(
    ShopCategoryView,
    ShopCategoryDetails
)



urlpatterns = [
    path('shop-category/', ShopCategoryView.as_view()),
    path('shop-category/<str:_id>/', ShopCategoryDetails.as_view()),
]
