from django.shortcuts import render, get_object_or_404, redirect

from cart.forms.payment_form import PaymentCreateForm
from cart.models import Order
from cart.forms.contact_form import ContactCreateForm


def index(request):
    # context = {'orders': Order.objects.get(pk=1)}
    try:
        context = {'orders': Order.objects.get(order_user=request.user, completed=False)}
    except Order.DoesNotExist:
        context = {'orders': Order.objects.create(order_user=request.user)}
    return render(request, 'cart/index.html', context)


def order(request):
    context = {}
    return render(request, 'cart/order.html', context)


def create_contact(request):
    if request.method == 'POST':
        form = ContactCreateForm(data=request.POST)
        if form.is_valid():
            current_order = Order.objects.get(order_user=request.user, completed=False)
            contact = form.save()
            current_order.contact_information = contact
            current_order.save()
            return redirect('create_payment')
    else:
        form = ContactCreateForm()
    return render(request, 'cart/create_contact.html', {
        'form': form
    })


def create_payment(request):
    if request.method == 'POST':
        form = PaymentCreateForm(data=request.POST)
        if form.is_valid():
            current_order = Order.objects.get(order_user=request.user, completed=False)
            payment = form.save()
            current_order.contact_information = payment
            current_order.save()
            return redirect('cart-index')  # change later to cart-review
    else:
        form = PaymentCreateForm()
    return render(request, 'cart/create_payment.html', {
        'form': form
    })
