from django.shortcuts import render, get_object_or_404

from offers.models import Offer


# Create your views here.


def index(request):
    context = {'offers': Offer.objects.all().order_by('name')}
    return render(request, 'offers/index.html', context)

def get_offer_by_id(request, id):
    return render(request, 'offers/add_to_cart.html', {
        'offer': get_object_or_404(Offer, pk=id)
    })