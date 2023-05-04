from django.shortcuts import render
import config


def index(request):
    return render(request, 'cart/index.html')
