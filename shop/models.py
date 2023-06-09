from django.db import models
import uuid
from user_account.models import(
    User
)
from django.utils.text import slugify

from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class ShopCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250,unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=250, unique=True, null=False, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"

class Shop(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops", null=True, blank=False)
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name="category", null=True, blank=False)
    is_active = models.BooleanField(default=False, null=True, blank=True) 
    connection = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    


class Connection(models.Model):
    CONEECTION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted')
    ]

    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="sender")
    reciver = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="reciver")
    status = models.CharField(max_length=50, choices=CONEECTION_STATUS_CHOICES, null=True, blank=True, default="pending")


    def __str__(self):
        return f"{self.pk}.Sender:{self.sender},Reciver:{self.reciver}"
    

@receiver(pre_save, sender=Shop)
@receiver(pre_save, sender=ShopCategory)
def update_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)

# Register the pre_save signal
pre_save.connect(update_slug, sender=Shop)
pre_save.connect(update_slug, sender=ShopCategory)



