from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



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



    path('', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'), 

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
