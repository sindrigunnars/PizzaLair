import uuid

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    screen_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.CharField(max_length=9999)
