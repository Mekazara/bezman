from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
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

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')

    context = {}
    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

def task1(request):
    string = 'fhksklhka'
    lst = []
    for letter in string:
        if letter not in lst:
            lst.append(letter)
        else:
            continue
    x = len(lst)
    if x % 2 == 0:
        return HttpResponse(['Chat with her!', string])
    else:
        return HttpResponse(['Ignore him', string])

def task2(request):
    string = 'gfgjhkhafjd'
    if len(set(string)) % 2 == 0:
        return HttpResponse(['Chat with her!', string])
    else:
        return HttpResponse(['Ignore him', string])

def task3(request):
    import random
    n, h = 3, 7
    list1 = []
    list2 =[]
    for i in range(n):
        list1.append(random.randint(1, 2*h))
    for x in list1:
        if x > h:
            list2.append(2)
        elif x <= h:
            list2.append(1)

    return HttpResponse([list1, sum(list2)])






