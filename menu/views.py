from django.shortcuts import render

# Create your views here.
pizzas = [
    {'name': 'Margarita','price': 2390},
    {'name': 'Pepperoni','price': 2890},
    {'name': 'Hawaiian','price': 2890}
]

def index(request):
    return render(request, 'menu/index.html', context={ 'pizzas': pizzas })
