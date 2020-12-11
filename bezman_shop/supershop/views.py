from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django_filters.filters import OrderingFilter
from .filters import ProductFilter
from .decorator import allowed_roles


# Create your views here.

def productList(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=products)
    products = filter.qs
    context = {'products': products, 'filter': filter}
    return render(request, 'supershop/products.html', context)


@allowed_roles(allowed=['bezman'])
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
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Page status = 404')
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
    try:
        order = Orders.objects.get(id=order_id)
    except Orders.DoesNotExist:
        return HttpResponse('Page status = 404')
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}

    return render(request, 'supershop/ordercreate.html', context)


def orderDelete(request, order_id):
    try:
        order = Orders.objects.get(id=order_id)
    except Orders.DoesNotExist:
        return HttpResponse('Page status = 404')
    form = OrderForm(instance=order)
    context = {'order': order}
    if request.method == 'POST':
        if order.status == 'New order':
            order.delete()
            return HttpResponse('Deleted')
        else:
            return HttpResponse('Something wrong')

    return render(request, 'supershop/order-delete.html', context)
