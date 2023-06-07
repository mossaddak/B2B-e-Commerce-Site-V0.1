from django.contrib import admin
from django.urls import path, include
from .views import(
    ProductView
)


urlpatterns = [
    path('add/', ProductView.as_view()),
]
