from django.db import models
from django.contrib import auth



class User(auth.models.AbstractUser):
    pass
