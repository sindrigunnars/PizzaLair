from django.db import models
from userprofile.models import User
from menu.models import Pizza
from offers.models import Offer


class Country(models.Model):
    name = models.CharField(max_length=255)


class ContactInformation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PaymentInformation(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    expiry = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    offers = models.ManyToManyField(Offer)
    price = models.FloatField()
    credit_card = models.ForeignKey(PaymentInformation, null=True, on_delete=models.DO_NOTHING)
    contact_information = models.ForeignKey(ContactInformation, null=True, on_delete=models.DO_NOTHING)
