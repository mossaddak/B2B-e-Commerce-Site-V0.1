from django.contrib import admin
from django.urls import path
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView,
    ProfileView,
    ProfilePictureView,
    VerifiCationOtpSentView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r"profile-picture", ProfilePictureView)

urlpatterns = [
    path('sing-up', SingUp.as_view()),
    path('login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('verification', VerifyOTPview.as_view()),
    path('send-code', VerifiCationOtpSentView.as_view()),
]+router.urls