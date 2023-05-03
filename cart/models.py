from django.db import models
from userprofile.models import User
from menu.models import Pizza
from offers.models import NewOrder


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)


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


class OrderPizza(models.Model):
    item = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(null=True, blank=True)


class OrderOffer(models.Model):
    item = models.ForeignKey(NewOrder, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(null=True, blank=True)


class Order(models.Model):
    pizzas = models.ManyToManyField(OrderPizza)
    offers = models.ManyToManyField(OrderOffer)
    price = models.FloatField(null=True, blank=True)
    credit_card = models.ForeignKey(PaymentInformation, null=True, on_delete=models.SET_NULL)
    contact_information = models.ForeignKey(ContactInformation, null=True, on_delete=models.SET_NULL)
