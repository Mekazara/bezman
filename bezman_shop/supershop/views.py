from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def productList(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'supershop/products.html', context)


def orderList(request):
    orders = Orders.objects.all()
    context = {'orders': orders}
    return render(request, 'supershop/orders.html', context)


def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)
    form = OrderForm(initial={'product': product})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'supershop/ordercreate.html', context)