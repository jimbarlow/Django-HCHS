from django.db import models
from django.urls import reverse
from typing import Any
from xmlrpc.client import boolean
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class VolunteerRolesCatalog(models.Model):
    volunteer_role_catalog_description = models.CharField(null=True, blank=True, max_length=200)
    vol_role_catalog = models.CharField(max_length=50)
    # date_entered = models.DateField(null=True, blank=True, default=timezone.now)

    def __str__(self):
      return self.vol_role_catalog 
    

  
class Volunteer(models.Model):

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    cell_phone = models.CharField(blank=True, max_length=15)
    email = models.EmailField(blank=True)
    home_phone = models.CharField(blank=True, max_length=15)
    date_entered = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    address = models.CharField(blank=True, max_length=100)
    emergency_contact_name = models.CharField(blank=True, max_length=100)
    emergency_contact_phone = models.CharField(blank=True, max_length=15)
    animals_preference = models.CharField(blank=True, max_length=100)
    disclaimer_signed = models.BooleanField(blank=True, default=False)
    status_notes = models.CharField(blank=True, max_length=2048)
    active = models.BooleanField(blank=True, default=False)
    volunteer_role = models.ManyToManyField(VolunteerRolesCatalog, related_name="volunteer_role" )
    volunteer_preferred_times = models.TextField(blank=True)
    other_notes = models.TextField(blank=True)

    def __str__(self):
        return self.first_name+' '+self.last_name
    
class Session(models.Model):
    session_name = models.CharField(max_length=100, null=True, blank=True)
    session_date = models.DateField()
    session_time = models.TimeField()
    session_volunteers = models.ManyToManyField(Volunteer, related_name="volunteers")
    session_notes = models.TextField()
    session_status = models.BooleanField(default=False)
    session_date_entered = models.DateTimeField(default=timezone.now)
    session_date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.session_name

class Tickets(models.Model):
    ticket_path = models.CharField(max_length=300)
    

    
