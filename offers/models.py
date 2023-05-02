from django.db import models
from menu.models import Pizza


class Offer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=9999)
    items = models.ManyToManyField(Pizza)
