from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', orderList, name='orders'),
    path('ordercreate/<int:product_id>/', orderCreate, name='ordercreate'),
    path('orderupdate/<int:order_id>/', orderUpdate, name='orderupdate'),
    path('orderdelete/<int:order_id>/', orderDelete, name='orderdelete'),
]
