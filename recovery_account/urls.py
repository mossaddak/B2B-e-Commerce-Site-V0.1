from django.contrib import admin
from django.urls import path
from .views import (
    PasswordReset,
    ResetPasswordSendTokenApi
)

urlpatterns = [
    path('otp-sent', PasswordReset.as_view(), name="otp-sent"),
    path('set-new-password',ResetPasswordSendTokenApi.as_view(), name="set-new-password"),
]
