from django.contrib import admin
from django.urls import path, include
from .views import(
    ProductView,
    MyProductView
)


urlpatterns = [
    path('add/', ProductView.as_view()),
    path('my-products/', MyProductView.as_view()),
]
