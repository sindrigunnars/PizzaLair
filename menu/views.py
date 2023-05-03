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
