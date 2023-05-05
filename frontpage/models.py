from django.db import models
from cart.models import Country


class Location(models.Model):
    address = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    opening_time = models.CharField(max_length=255, default="11:00-23:00")


class Information(models.Model):
    locations = models.ManyToManyField(Location)
    about_us = models.CharField(max_length=9999)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)