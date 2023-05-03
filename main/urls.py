from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as authViews
from django.urls import include, path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls') ),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/', include('orders.urls', namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls',namespace='payment' )),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls', namespace='shop')),
    
   
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
