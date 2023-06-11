from django.contrib import admin
from django.urls import path, include
from .views import(
    ProductView,
    ProductDetailsView,
    AllProductView
)


urlpatterns = [
    path('s', AllProductView.as_view()),
    path('s/me', ProductView.as_view()),
    path('s/me/<str:slug>', ProductDetailsView.as_view()),
]
