from django.urls import path

from . import views
app_name='orders'

urlpatterns = [
    path(r'^create/$', views.order_create, name='order_create'),
    path(r'^process/$', views.order_save, name='order_save'),

]