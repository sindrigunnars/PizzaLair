from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from menu.models import Pizza
from offers.models import NewOrder
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ContactInformation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    house_number = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=255)
    zip = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(9999)])
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class PaymentInformation(models.Model):
    name = models.CharField(max_length=255)
    card_number = CardNumberField('card number')
    cvc = SecurityCodeField('security code')
    expiry = CardExpiryField('expiration date')


class OrderPizza(models.Model):
    item = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(default=1)


class OrderOffer(models.Model):
    item = models.ForeignKey(NewOrder, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(default=1)


class Order(models.Model):
    pizzas = models.ManyToManyField(OrderPizza)
    offers = models.ManyToManyField(OrderOffer)
    completed = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    credit_card = models.ForeignKey(PaymentInformation, null=True, on_delete=models.SET_NULL)
    contact_information = models.ForeignKey(ContactInformation, null=True, on_delete=models.SET_NULL)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
