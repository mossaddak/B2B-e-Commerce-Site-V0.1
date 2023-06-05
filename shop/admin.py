from django.contrib import admin
from .models import (
    ShopCategory,
    Shop,
    Connection
)

# Register your models here.
admin.site.register(ShopCategory)
admin.site.register(Shop)
admin.site.register(Connection)
