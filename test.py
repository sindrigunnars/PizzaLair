from menu.models import Pizza
from offers.models import Offer

pizzas = Pizza.objects.all()
offer = Offer.objects.get(name="2 for 1")



