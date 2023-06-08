from django.contrib import admin
from django.urls import path, include
from .views import(
    OrderProductView,
    MyOrderView
)


urlpatterns = [
    path("order-products", OrderProductView.as_view()),
    path("my-orders", MyOrderView.as_view()),
]
