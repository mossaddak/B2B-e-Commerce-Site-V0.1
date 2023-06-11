from django.db import models
import uuid
from shop.models import(
    Shop
)
from cart.models import(
    ShoppingCart
)

class ProductStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    DELIVERED = "DELIVERED", "Delivered"

# Create your models here.
class OrderProduct(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    cart_items = models.TextField(blank=True)
    total_qty = models.IntegerField(blank=True)
    total_price = models.PositiveIntegerField(blank=True)
    status = models.CharField(max_length=50,blank=True, choices=ProductStatus.choices, default=ProductStatus.PENDING)
    is_pay = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.pk},{self.shop}"

