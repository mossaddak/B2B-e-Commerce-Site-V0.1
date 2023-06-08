from django.contrib import admin
from django.urls import path, include
from .views import(
    ShoppingCartView,
    MyCartView
)


urlpatterns = [
    path('add', ShoppingCartView.as_view()),
    path('my-carts', MyCartView.as_view()),
]
