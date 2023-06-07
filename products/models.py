from django.db import models
from django.core.validators import MinValueValidator
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.models import(
    Shop
)

# Create your models here.
class Product(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=False, related_query_name="products")
    title = models.CharField(null=True, blank=False, max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        f"{self.pk},{self.title}"




@receiver(pre_save, sender=Product)
def update_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)

# Register the pre_save signal
pre_save.connect(update_slug, sender=Product)

