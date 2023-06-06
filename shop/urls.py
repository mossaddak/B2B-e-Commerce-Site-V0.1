from django.contrib import admin
from django.urls import path, include
from .views import(
    ShopCategoryView,
    ShopCategoryDetails,
    ShopView,
    ShopDetailsView,
    ActivateShopView,
    AllShopView
)



urlpatterns = [
    #category
    path('shop-category/', ShopCategoryView.as_view()),
    path('shop-category/<str:slug>/', ShopCategoryDetails.as_view()),

    #shop
    path('shop/', ShopView.as_view()),
    path('shop/<str:slug>/', ShopDetailsView.as_view()),
    path('activate/', ActivateShopView.as_view()),
    path('all-shop/', AllShopView.as_view()),
]
