from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Order
from cart.forms.contact_form import ContactCreateForm
import config


def index(request):
    context = {'orders': Order.objects.get(pk=1)}
    return render(request, 'cart/index.html', context)


def order(request):
    context = {}
    return render(request, 'cart/order.html', context)


def create_contact(request):
    if request.method == 'POST':
        form = ContactCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart-index') #change later to create_payment
    else:
        form = ContactCreateForm()
    return render(request, 'cart/create_contact.html', {
        'form': form
    })
