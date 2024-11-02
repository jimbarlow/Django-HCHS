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
    date_entered = models.DateField(auto_now_add=True)

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
    
class CareSession(models.Model):
    
    care_session_date = models.DateField()
    care_session_slot = models.TextField(models.Model)
    care_session_volunteers = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    session_notes = models.TextField()
    changed_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.care_session_date + ' ' + self.care_session_slot

class Tickets(models.Model):
    ticket_path = models.CharField(max_length=300)

   
