from django.db import models
from django.contrib import auth



class User(auth.models.AbstractUser):
    pass




class GhostName(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
