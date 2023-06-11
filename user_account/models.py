from django.db import models
from django.contrib.auth.models import User
from .manager import CustomeUserManager
from django.contrib.auth.models import AbstractUser
import uuid




# Create your models here.
class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('merchant', 'Merchant')
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"A user with that email already exists."})
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=20, null=True, blank=True)
    password_reset_token = models.CharField(max_length=20, null=True, blank=True)
    is_subscribed = models.BooleanField(default=False)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES, default="merchant")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'username']
    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.username}"
    
    class Meta:
        verbose_name_plural = 'Merchant'
    
class ProfilePicture(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_picture")
    image = models.ImageField()

    def __str__(self):
        return f"{self.pk},{self.user}"
    
    
