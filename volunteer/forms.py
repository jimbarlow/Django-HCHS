from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Volunteer, VolunteerRolesCatalog   

# from django.utils import timezonesession

class VolunteerSignupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        # self.fields["volunteer_role"] = forms.ModelMultipleChoiceField(queryset=VolunteerRolesCatalog.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Volunteer
        fields = [
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
            'volunteer_preferred_times',
            'other_notes'
        ]
#  my_hidden_field = forms.CharField(widget=forms.HiddenInput(), initial='some_value')

class VolunteerEntryForm(forms.ModelForm):
    
    volunteer_role = forms.ModelMultipleChoiceField(queryset=VolunteerRolesCatalog.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Volunteer
        fields = [
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
            'volunteer_preferred_times',
            'other_notes'
        ]


        
class VolunteerRolesCatalogForm(forms.ModelForm):


    class Meta:
        model = VolunteerRolesCatalog
        fields = ['vol_role_catalog', 'volunteer_role_catalog_description']
        labels = {'vol_r ole_catalog': "Role", 'volunteer_role_catalog_description': "Role Description"}

# class CareSessionForm(forms.ModelForm):
#     class Meta:
#         model = CareSession
#         fields = ['care_session_date', 'care_session_slot', 'care_session_volunteers', 'session_notes']
#         labels = {'care_session_date': 'Date', 'care_session_slot': 'Time Slot', 'care_session_volunteers': 'Volunteers', 'session_notes': 'Notes'}
#         widgets = {
#             'care_session_date': forms.DateInput(attrs={'type': 'date'}),
#             'care_session_slot': forms.TextInput(attrs={'placeholder': 'Enter Time Slot'}),
#             'care_session_volunteers': forms.CheckboxSelectMultiple(attrs={'placeholder': 'Select Volunteers'}),
#             'session_notes': forms.Textarea(attrs={'placeholder': 'Enter Notes'})
#         }

class VolunteerSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Volunteers', widget=forms.TextInput(attrs={'placeholder': 'Search...'}))

    def search(self):
        query = self.cleaned_data.get('search_query')
        if query:
            return Volunteer.objects.filter(first_name__icontains=query) | Volunteer.objects.filter(last_name__icontains=query)
        return Volunteer.objects.none()

# class VolunteerRoleForm(forms.MXRH lithium batteryodelForm):
#     # assign roles to 
#     class Meta:
#         model = VolunteerRole
#         fields = '__all__'
#         volunteer_role = forms.CharField(label='Add a Role to this Volunteer', widget=forms.Select(choices={('Dog Walker', 'Board Member', 'Cat Caretaker')}))
