from typing import Optional
from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class register(models.Model):
    name = models.CharField( max_length=50 , unique= True)
    password = models.CharField( max_length=50 , unique=True)
    email = models.EmailField( max_length=254, unique= True)
    remember_this_credentials = models.BooleanField()
