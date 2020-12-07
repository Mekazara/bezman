from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', customerList, name='customers'),
    path('customer/<int:customer_id>/', getCustomer, name='getcustomer'),
    path('user-create/', createUser, name='user-create'),
    path('login/', auth, name='login'),
    path('logout/', logout_page,name='logout')
]
