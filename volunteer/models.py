from django.db import models
from django.urls import reverse
from typing import Any
from xmlrpc.client import boolean
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Volunteers(models.Model):

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    cell_phone = models.CharField(blank=True, max_length=15)
    email = models.EmailField(default='heyyou@example.com', blank=True)
    home_phone = models.CharField(blank=True, max_length=15)
    date_entered = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    address = models.CharField(blank=True, max_length=100)
    emergency_contact_name = models.CharField(blank=True, max_length=100)
    emergency_contact_phone = models.CharField(blank=True, max_length=15)
    animals_preference = models.CharField(blank=True, max_length=100)
    disclaimer_signed = models.BooleanField(blank=True, default=False)
    active = models.BooleanField(blank=True, default=False)
 
    # newmanager = models.Manager()

    def __str__(self):
        return self.first_name+' '+self.last_name
    
    