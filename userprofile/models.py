from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    screen_name = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=9999, null=True)

    def __str__(self):
        return self.screen_name
