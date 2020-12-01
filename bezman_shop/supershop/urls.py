from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', productList, name='products'),
    path('orders/', orderList, name='orders'),
    path('orderform/', orderForm),
]
