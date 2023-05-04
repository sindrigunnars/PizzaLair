from django.shortcuts import render
from frontpage.models import *


def index(request):
    return render(request, 'frontpage/index.html')


def about_us(request):
    context = {
        "information": Information.objects.get(pk=1)
    }
    return render(request, 'frontpage/about_us.html', context)


def locations(request):
    context = {
        "information": Information.objects.get(pk=1)
    }
    return render(request, 'frontpage/locations.html', context)


def contact_us(request):
    context = {
        "information": Information.objects.get(pk=1)
    }
    return render(request, 'frontpage/contact_us.html', context)
