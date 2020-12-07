from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter


# Create your views here.

def productList(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=products)
    products = filter.qs
    context = {'products': products, 'filter': filter}
    return render(request, 'supershop/products.html', context)


def orderList(request):
    orders = Orders.objects.all()
    orders_count = orders.count()
    orders_new = Orders.objects.filter(status='New order').count()
    orders_delivered = Orders.objects.filter(status='Delivered').count()
    orders_in_process = Orders.objects.filter(status='In process').count()
    orders_not_delivered = Orders.objects.filter(status='Not delivered').count()
    context = {'orders': orders,
               "orders_count": orders_count,
               'orders_new': orders_new,
               'orders_delivered': orders_delivered,
               'orders_in_process': orders_in_process,
               'orders_not_delivered': orders_not_delivered,
               }
    return render(request, 'supershop/orders.html', context)


def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user
    form = OrderForm(initial={'product': product, 'customer_order': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'supershop/ordercreate.html', context)

def orderUpdate(request, order_id):
    order = Orders.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}

    return render(request, 'supershop/ordercreate.html', context)

