from django.db import models
from menu.models import Pizza


class Offer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=9999, blank=True, null=True)


class NewOrder(models.Model):
    order = models.ForeignKey(Offer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Pizza)
