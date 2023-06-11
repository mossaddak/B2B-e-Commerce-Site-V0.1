from django.contrib import admin
from django.urls import path, include
from .views import(
    ShoppingCartView,
    MyCartView
)


urlpatterns = [
    path('s', ShoppingCartView.as_view()),
    path('s/me', MyCartView.as_view()),
]
