from django.contrib import admin
from django.urls import path, include
from .views import(
    ProductView,
    MyProductView,
    ProductDetailsView,
    AllProductView
)


urlpatterns = [
    path('add/', ProductView.as_view()),
    path('my-products', MyProductView.as_view()),
    path('products', AllProductView.as_view()),
    path('products/<str:slug>', ProductDetailsView.as_view()),
]
