from django.contrib import admin
from django.urls import path, include
from .views import(
    ShoppingCartView
)


urlpatterns = [
    path('add', ShoppingCartView.as_view()),
]
