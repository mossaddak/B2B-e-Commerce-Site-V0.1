from django.db import models
import uuid
from user_account.models import(
    User
)

# Create your models here.
class ShopCategory(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    

# class Shop(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops", null=True, blank=False)
#     category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name="category", null=True, blank=False)


