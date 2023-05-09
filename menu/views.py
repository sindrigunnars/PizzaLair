from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Order, OrderPizza
from menu.models import Pizza, PizzaType


# Create your views here.
# pizzas = [
#     {'name': 'Margarita', 'price': 2390},
#     {'name': 'Pepperoni', 'price': 2890},
#     {'name': 'Hawaiian', 'price': 2890}
# ]


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id': x.pk,
            'name': x.name,
            'price': x.price,
            'image': x.images.all()[0].image
        } for x in list(Pizza.objects.filter(name__icontains=search_filter))]
        return JsonResponse({'data': pizzas})
    if 'sort_name' in request.GET:
        pizzas = [{
            'id': x.pk,
            'name': x.name,
            'price': x.price,
            'image': x.images.all()[0].image
        } for x in list(Pizza.objects.all().order_by('name'))]
        return JsonResponse({'data': pizzas})
    if 'sort_price' in request.GET:
        pizzas = [{
            'id': x.pk,
            'name': x.name,
            'price': x.price,
            'image': x.images.all()[0].image
        } for x in list(Pizza.objects.all().order_by('-price'))]
        return JsonResponse({'data': pizzas})
    if 'filter' in request.GET:
        type_name = request.GET['filter']
        pizzas = [{
            'id': x.pk,
            'name': x.name,
            'price': x.price,
            'image': x.images.all()[0].image
        } for x in list(Pizza.objects.filter(type=PizzaType.objects.get(name=type_name).id))]
        return JsonResponse({'data': pizzas})
    context = {
        'pizzas': Pizza.objects.all().order_by('name'),
        'types': PizzaType.objects.all()
    }
    return render(request, 'menu/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'menu/single_pizza.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def add_menu_to_cart(request):
    try:
        pizza_id = request.POST['pizzaId']
        cart_order = Order.objects.get(order_user=request.user, completed=False)
        for pizza in cart_order.pizzas.all():
            if int(pizza.item_id) == int(pizza_id):
                pizza.amount += 1
                pizza.save()
                return redirect('menu-index')
        cart_order.pizzas.add(OrderPizza.objects.create(item=Pizza.objects.get(pk=pizza_id)))
        cart_order.price += Pizza.objects.get(pk=pizza_id).price
        cart_order.save()
    except Order.DoesNotExist:
        new_order = Order.objects.create(order_user=request.user)
        new_order.pizzas.add(OrderPizza.objects.create(item=Pizza.objects.get(pk=pizza_id)))
        new_order.price += Pizza.objects.get(pk=pizza_id).price
        new_order.save()
    except TypeError:
        return redirect('login')
    return redirect('menu-index')

"""
def search(request):
    search = request.GET.get('q')
    if search:
        pizzas = Pizza.objects.filter(name__icontains=search)
    else:
        return redirect('menu-index')
    return render(
        request=request,
        template_name='menu/index.html',
        context={
            'pizzas': pizzas
        }
    )
"""

"""
def order_by(request):
    order_by = request.GET.get('q')
    if search:
        pizzas = Pizza.objects.all().order_by(order_by)
    else:
        return redirect('menu-index')
    return render(
        request=request,
        template_name='menu/index.html',
        context={
            'pizzas': pizzas
        }
    )
"""
