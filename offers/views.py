from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import Order, OrderOffer
from menu.models import Pizza
from .models import Offer, NewOrder, OrderItem


# Create your views here.


def index(request):
    context = {
        'offers': Offer.objects.all().order_by('name'),
    }
    return render(request, 'offers/index.html', context)


def get_offer_by_id(request, id):
    return render(request, 'offers/add_to_cart.html', {
        'offer': get_object_or_404(Offer, pk=id),
        'pizzas': Pizza.objects.all()
    })


def get_pizza_by_id(request, id):
    return render(request, 'offers/add_to_cart.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def add_offer_to_cart(request):
    pizza1, pizza2, offer_id = request.POST['pizza1'], request.POST['pizza2'], request.POST['OfferID']
    pizza_object1, pizza_object2 = Pizza.objects.get(pk=pizza1), Pizza.objects.get(pk=pizza2)
    new_offer = NewOrder.objects.create(order=Offer.objects.get(pk=offer_id))
    new_offer.items.add(OrderItem.objects.create(item=pizza_object1), OrderItem.objects.create(item=pizza_object2))
    new_offer.price = pizza_object1.price if pizza_object1.price > pizza_object2.price else pizza_object2.price
    new_offer.save()
    try:
        cart_order = Order.objects.get(order_user=request.user, completed=False)
        cart_order.offers.add(OrderOffer.objects.create(item=new_offer))
        cart_order.price += new_offer.price
        cart_order.save()
    except Order.DoesNotExist:
        new_order = Order.objects.create(order_user=request.user)
        new_order.offers.add(OrderOffer.objects.create(item=new_offer))
        new_order.price += new_offer.price
        new_order.save()
    except TypeError:
        return redirect('login')
    return redirect('offers-index')
