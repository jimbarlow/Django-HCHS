from django.db import models
from django.urls import reverse
from typing import Any
from xmlrpc.client import boolean
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Adopter(models.Model):

    current_pet_name = models.CharField(max_length=200)
    current_pet_status = models.CharField(max_length=200)
    current_application_status = models.CharField(max_length=200)
    adopter_first_name = models.CharField(max_length=200)
    adopter_last_name = models.CharField(max_length=200)
    adopter_address = models.CharField(max_length=200)
    adopter_email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.adopter_first_name+' '+self.adopter_last_name
    
