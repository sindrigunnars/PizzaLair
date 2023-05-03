from django.shortcuts import render
from menu.models import Pizza

# Create your views here.
pizzas = [
    {'name': 'Margarita', 'price': 2390},
    {'name': 'Pepperoni', 'price': 2890},
    {'name': 'Hawaiian', 'price': 2890}
]


def index(request):
    context = {'pizzas': Pizza.objects.all()}
    return render(request, 'menu/index.html', context)


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
