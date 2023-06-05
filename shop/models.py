from django.db import models
import uuid
from user_account.models import(
    User
)
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class ShopCategory(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250,unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
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

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)




    # def save(self, *args, **kwargs):
    #     if not self.slug or self.title != self.slugify(self.title):
    #         self.slug = self.slugify(self.title)
    #     super().save(*args, **kwargs)
    
    # def slugify(self, value):
    #     return slugify(value)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    

@receiver(pre_save, sender=Shop)
def update_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


# Register the pre_save signal
pre_save.connect(update_slug, sender=Shop)
    

class Connection(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="sender")
    reciver = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="reciver")

    def __str__(self):
        return f"{self.pk}.Sender:{self.sender},Reciver:{self.reciver}"



