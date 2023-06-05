from django.contrib import admin
from django.urls import path, include
from .views import(
    ShopCategoryView,
    ShopCategoryDetails,
    ShopView
)



urlpatterns = [
    path('shop-category/', ShopCategoryView.as_view()),
    path('shop-category/<str:slug>/', ShopCategoryDetails.as_view()),
    path('create-shop/', ShopView.as_view()),
]
