from django.shortcuts import render, get_object_or_404
from cart.models import Order
import config


def index(request):
    context = {'orders': Order.objects.all()}
    return render(request, 'cart/index.html', context)


def order(request):
    context = {}
    return render(request, 'cart/order.html', context)
