from django.shortcuts import render, get_object_or_404
from menu.models import Pizza

# Create your views here.
# pizzas = [
#     {'name': 'Margarita', 'price': 2390},
#     {'name': 'Pepperoni', 'price': 2890},
#     {'name': 'Hawaiian', 'price': 2890}
# ]


def index(request):
    context = {'pizzas': Pizza.objects.all().order_by('name')}
    return render(request, 'menu/index.html', context)

def get_pizza_by_id(request, id):
    return render(request, 'menu/single_pizza.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })

def search(request):
    search = request.GET.get('q')
    if search:
        pizzas = Pizza.objects.filter(name__icontains=search)
    else:
        pizzas = Pizza.objects.none()
    return render(
        request=request,
        template_name='menu/index.html',
        context={
            'pizzas': pizzas
        }
    )
