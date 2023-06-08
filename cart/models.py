from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from products.models import(
    Product
)
from shop.models import(
    Shop
)

# Create your models here.
class ShoppingCart(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shopping_carts", null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carts", blank=False, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True, blank=False)
    totalPrice = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return f"{self.pk}.{self.product}"