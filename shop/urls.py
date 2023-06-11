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
    AcceptConnectView,
    ConnectedShopView
)



urlpatterns = [
    #category
    path('categories', ShopCategoryView.as_view()),
    path('categories/<str:slug>', ShopCategoryDetails.as_view()),

    #shop
    path('me/shops', ShopView.as_view()),
    path('me/shops/<str:slug>', ShopDetailsView.as_view()),
    path('me/shops/activate/', ActivateShopView.as_view()),
    path('me/shops/connected/', ConnectedShopView.as_view()),
    path('shops', AllShopView.as_view()),
    path('shops/connection', ShopConnectView.as_view()),
    path('shop/connection/accepted', AcceptConnectView.as_view()),
    
]
 