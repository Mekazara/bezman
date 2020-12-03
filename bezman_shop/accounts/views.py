from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def customerList(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/customers.html', context)


def getCustomer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.orders_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'accounts/getcustomer.html', context)


def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context = {'form': form}
    return render(request, 'accounts/user-create.html', context)

# def createCustomer(request):
#     form =