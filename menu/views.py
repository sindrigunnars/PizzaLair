from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza

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
    context = {'pizzas': Pizza.objects.all().order_by('name')}
    return render(request, 'menu/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'menu/single_pizza.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })

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
