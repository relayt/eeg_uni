from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    affiliation = models.CharField(max_length=64, blank=True)
