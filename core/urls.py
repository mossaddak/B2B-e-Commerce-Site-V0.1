from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #user account
    path('api/user-account/', include("user_account.urls")),

    #recovery account
    path('api/recovery-account/', include("recovery_account.urls")),

    #shop
    path('api/shop/', include("shop.urls")),

    #product
    path('api/product/', include("products.urls")),

    #cart
    path('api/cart/', include("cart.urls")),

    #cart
    path('api/orders/', include("orders.urls")),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
