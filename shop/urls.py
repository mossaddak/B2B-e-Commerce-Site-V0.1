from django.contrib import admin
from django.urls import path, include
from .views import(
    ShopCategoryView
)



urlpatterns = [
    path('shop-category/', ShopCategoryView.as_view())
]
