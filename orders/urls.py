from django.contrib import admin
from django.urls import path, include
from .views import(
    OrderProductView
)


urlpatterns = [
    path("order-product", OrderProductView.as_view())
]
