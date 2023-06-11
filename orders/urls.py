from django.contrib import admin
from django.urls import path, include
from .views import(
    OrderProductView,
    MyOrderView
)


urlpatterns = [
    path("s", OrderProductView.as_view()),
    path("s/me", MyOrderView.as_view()),
]
