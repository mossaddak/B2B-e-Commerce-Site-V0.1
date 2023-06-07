from django.db import models
from django.core.validators import MinValueValidator
import uuid
from products.models import(
    Product
)

# Create your models here.
class ShoppingCart(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carts", blank=False, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=False)
    totalPrice = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return f"{self.pk},{self.product}"