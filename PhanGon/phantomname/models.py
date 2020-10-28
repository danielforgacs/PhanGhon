from django.db import models
from django.contrib import auth



class User(auth.models.AbstractUser):
    pass




class GhostName(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)




class PhantomName(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    ghostname = models.ForeignKey(to='GhostName', on_delete=models.CASCADE)
