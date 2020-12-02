from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/', customerList),
    path('accounts/<int:customer_id>/', getCustomer, name='getcustomer')
]
