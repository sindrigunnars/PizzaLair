from django.shortcuts import render

from offers.models import Offer


# Create your views here.


def index(request):
    context = {'offers': Offer.objects.all()}
    return render(request, 'offers/index.html', context)