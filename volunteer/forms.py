from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Volunteer, VolunteerRolesCatalog

from django.utils import timezone

class VolunteerEntryForm(forms.ModelForm):
    
    volunteer_role = forms.ModelMultipleChoiceField(queryset=VolunteerRolesCatalog.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Volunteer
        fields = (
            'first_name', 
            'last_name', 
            'cell_phone',
            'email',
            'home_phone',
            'address',
            'emergency_contact_name',
            'emergency_contact_phone',
            'animals_preference',
            'disclaimer_signed',
            'active',
            'volunteer_role',
        )


        
class VolunteerRolesCatalogForm(forms.ModelForm):


    class Meta:
        model = VolunteerRolesCatalog
        fields = ['vol_role_catalog', 'volunteer_role_catalog_description']
        labels = {'vol_role_catalog': "Role", 'volunteer_role_catalog_description': "Role Description"}


# class VolunteerRoleForm(forms.ModelForm):
#     # assign roles to 
#     class Meta:
#         model = VolunteerRole
#         fields = '__all__'
#         volunteer_role = forms.CharField(label='Add a Role to this Volunteer', widget=forms.Select(choices={('Dog Walker', 'Board Member', 'Cat Caretaker')}))
