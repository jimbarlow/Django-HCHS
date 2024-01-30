from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Volunteers

from django.utils import timezone

# class CreateMembershipEntry(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     last_name = forms.CharField(label="Last Name", max_length=100)
#     cell_phone = forms.CharField(label="Cell Phone", required=False, max_length=15)
#     email = forms.EmailField(label="Email Address", required=False, max_length=100)
#     hartwell_address = forms.CharField(label="Hartwell Address", max_length=100)
#     other_home_address = forms.CharField(required=False, max_length=100)
#     emergency_contact_name = forms.CharField(required=False, max_length=100)
#     emergency_contact_phone = forms.CharField(required=False, max_length=15)
#     home_phone = forms.CharField(label="Home Phone", required=False, max_length=15)
#     dues_paid_for_year = forms.CharField(label="Dues Paid for Year", required=False, max_length=4)
 
#     # checker_box = forms.BooleanField(required=False

class CreateVolunteersEntry(ModelForm):
    class Meta:
        model = Volunteers
        fields = '__all__'


class UpdateVolunteersEntry(ModelForm):
    class Meta:
        model = Volunteers
        fields = '__all__'
