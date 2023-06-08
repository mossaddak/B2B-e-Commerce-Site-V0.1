from django.db import models
from shop.models import(
    Shop
)
from cart.models import(
    ShoppingCart
)

# Create your models here.
class OrderProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False)
    cart_items = models.TextField(null=True, blank=False)
    is_pay = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.pk},{self.shop}"

