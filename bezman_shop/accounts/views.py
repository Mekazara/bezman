from django.shortcuts import render
from .models import *

# Create your views here.

def customerList(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/customers.html', context)

def getCustomer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    context = {'customer': customer}
    return render(request, 'accounts/getcustomer.html', context)
