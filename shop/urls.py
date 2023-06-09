from django.contrib import admin
from django.urls import path, include
from .views import(
    ShopCategoryView,
    ShopCategoryDetails,
    ShopView,
    ShopDetailsView,
    ActivateShopView,
    AllShopView,
    ShopConnectView,
    AcceptConnectView
)



urlpatterns = [
    #category
    path('categories', ShopCategoryView.as_view()),
    path('categories/<str:slug>', ShopCategoryDetails.as_view()),

    #shop
    path('shop/', ShopView.as_view()),
    path('shop/<str:slug>/', ShopDetailsView.as_view()),
    path('activate/', ActivateShopView.as_view()),
    path('all/', AllShopView.as_view()),
    path('connection/', ShopConnectView.as_view()),
    path('connection/accept/', AcceptConnectView.as_view()),
]
 