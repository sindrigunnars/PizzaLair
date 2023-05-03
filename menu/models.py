from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PizzaType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)


class Pizza(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    type = models.ForeignKey(PizzaType, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    toppings = models.ManyToManyField(Topping)
    images = models.ManyToManyField(PizzaImage)

    def __str__(self):
        return f"{self.name} - {self.price}"
