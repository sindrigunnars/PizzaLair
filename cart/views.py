from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from cart.forms.payment_form import PaymentCreateForm
from cart.models import Order, PaymentInformation
from cart.forms.contact_form import ContactCreateForm
from menu.models import Pizza


def index(request):
    if 'add-pizza' in request.GET:
        add_id = request.GET['add-pizza']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.pizzas.all().get(pk=add_id)
        order_item.amount += 1
        cust_order.price += Pizza.objects.get(pk=order_item.item_id).price
        order_item.save()
        cust_order.save()
        return JsonResponse({'data': [order_item.amount, cust_order.price]})
    if 'minus-pizza' in request.GET:
        minus_id = request.GET['minus-pizza']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.pizzas.all().get(pk=minus_id)
        order_item.amount -= 1
        cust_order.price -= Pizza.objects.get(pk=order_item.item_id).price
        order_item.save()
        cust_order.save()
        return JsonResponse({'data': [order_item.amount, cust_order.price]})
    if 'add-offer' in request.GET:
        add_id = request.GET['add-offer']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.offers.all().get(pk=add_id)
        order_item.amount += 1
        cust_order.price += order_item.item.price
        order_item.save()
        cust_order.save()
        return JsonResponse({'data': [order_item.amount, cust_order.price]})
    if 'minus-offer' in request.GET:
        minus_id = request.GET['minus-offer']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.offers.all().get(pk=minus_id)
        order_item.amount -= 1
        cust_order.price -= order_item.item.price
        order_item.save()
        cust_order.save()
        return JsonResponse({'data': [order_item.amount, cust_order.price]})
    if 'remove-pizza' in request.GET:
        remove_id = request.GET['remove-pizza']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.pizzas.all().get(pk=remove_id)
        cust_order.price -= order_item.amount * Pizza.objects.get(pk=order_item.item_id).price
        cust_order.save()
        order_item.delete()
        return JsonResponse({'data': cust_order.price})
    if 'remove-offer' in request.GET:
        remove_id = request.GET['remove-offer']
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        order_item = cust_order.offers.all().get(pk=remove_id)
        cust_order.price -= order_item.amount * order_item.item.price
        cust_order.save()
        order_item.delete()
        return JsonResponse({'data': cust_order.price})
    if 'clear-all' in request.GET:
        cust_order = Order.objects.get(order_user=request.user, completed=False)
        cust_order.delete()
        Order.objects.create(order_user=request.user)
        return JsonResponse({'data': cust_order.price})
    try:
        context = {'orders': Order.objects.get(order_user=request.user, completed=False)}
    except Order.DoesNotExist:
        context = {'orders': Order.objects.create(order_user=request.user)}
    return render(request, 'cart/index.html', context)


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
            current_order.payment_information = payment
            current_order.save()
            return redirect('review')
    else:
        form = PaymentCreateForm()
    return render(request, 'cart/create_payment.html', {
        'form': form
    })


'''def payment(request):
    context = {
        'information': PaymentInformation.objects.all()
    }'''


def review(request):
    context = {
        'order': Order.objects.get(order_user=request.user, completed=False),
    }
    return render(request, 'cart/review.html', context)


def payment(request):
    context = {
        'cc': PaymentInformation.objects.all()
    }
    return render(request, 'cart/review.html', context)