from django.db import models
import uuid
from user_account.models import(
    User
)
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.
class ShopCategory(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250, null=True, blank=True)
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
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name="category", null=True, blank=False)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    #request_sender = models.ForeignKey('Shop', null=True, blank=True, on_delete=models.CASCADE, related_name='request_senders')
    connection = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)


    def __str__(self):
        return f"{self.pk}.{self.title}"
    

class Connection(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="sender")
    reciver = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, related_name="reciver")

    def __str__(self):
        return f"{self.pk}.Sender:{self.sender},Reciver:{self.reciver}"



