from django.db import models
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
    img = models.ImageField(null=True, blank=True, upload_to="files/img/product")

    def __str__(self):
        return f"{self.pk}.{self.title}"


@receiver(pre_save, sender=Product)
def update_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)

# Register the pre_save signal
pre_save.connect(update_slug, sender=Product)

