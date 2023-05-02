from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=255)


class PizzaType(models.Model):
    name = models.CharField(max_length=255)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    toppings = models.ManyToManyField(Topping)


class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
