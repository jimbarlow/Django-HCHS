from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import user_passes_test, permission_required, login_required
from django.db import models
from django.template.loader import get_template
from django.template import Template, Context
from .models import Volunteer,  Tickets, VolunteerRolesCatalog
from django.urls import reverse
# Datetime stuff
import datetime
from django.http import HttpResponse
# from collections import Counter
from .forms import VolunteerEntryForm  # VolunteerRoleForm,
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
import os
# import pprint
# from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# for class based views:
from django.views import View
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from .forms import VolunteerRolesCatalogForm
# for Formtools multi form wizardry
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail, get_connection
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here./
# def front_page(request):
#     return render(request, 'front_page.html')

# class FrontPageView(View):
#     def get(self, request):
#         return HttpResponse(request, 'front_page.html' )

# class ModelFormWizard(SessionWizardView):
# # https://django-formtools.readthedocs.io/en/latest/wizard.html
#     template_name = 'modelwiz_entry.html'
#     # print(membership_id)
#     def done(self, form_list, **kwargs):
#         for form in form_list:
#             form.save()
#         return H        ttpResponseRedirect('home')

# def entry_form(request, membership_id, *args, **kwargs):

#     membership = Membership.newmanager.get(pk=membership_id)
#     print(membership.first_name + ' ' + membership.last_name)
    
#     MemberShipYearsFormset = inlineformset_factory(Membership, MemberShipYears, fields = ('year',), extra=1, )

#     if request.method == 'POST':
#         formset = MemberShipYearsFormset(request.POST, instance = membership)
#         if formset.is_valid():
#             formset.save()
#             # return redirect('entry_form/'+ str(formset.id)+ '/')
#             return redirect('entry_form', membership_id = membership_id)
#     formset = MemberShipYearsFormset(instance=membership)
#     return(render(request, 'formset.html', { 'formset' : formset, 'membership' : membership }))

   
@login_required(login_url='login')
def roster_by_role(request):

    obj_vol = Volunteer.objects.all().order_by('last_name','first_name')
    obj_role = VolunteerRolesCatalog.objects.all()

    context =  {
        'obj_role': obj_role,
        'obj_vol': obj_vol,
        'date_printed': datetime.date.today(),
    }

    return render(request, 'roster_by_role.html', context)

@login_required(login_url='login')
def roster_no_role(request):

    no_role_volunteer = Volunteer.objects.all().filter(volunteer_role=None).order_by('last_name','first_name')


    context =  {
        'no_role_volunteer': no_role_volunteer,
        'date_printed': datetime.date.today()
    }

    return render(request, 'roster_no_role.html', context)


@login_required(login_url='login')
def tickets(request):
    directory = 'static'

    file_names = []
    for filename in os.listdir(directory):
        # f = os.path.join(directory, filename)
        # checking if it is a file
        print ('Filename looped is:', filename)
        # if os.path.isfile(filename):
        #     print(filename)response
        #     # fabs = os.path.abspath(f)
        entry = Tickets(ticket_path = filename)
        entry.save()
        
    return HttpResponse('This is the ticket ingestion complete')
@login_required(login_url='login')
def print_tickets(request):
    obj = Tickets.objects.all()
    context = {
        'tickets': obj
        }
    return render(request, 'tickets.html', context)

@login_required(login_url='login')
def browse_roster(request):
# class CreateRolesEntry(forms.ModelForm):
#     class Meta:
#         model = VolunteerRole
#         fields = '__all__'
        
    obj = Volunteer.objects.all().order_by('last_name','first_name')


    # addresses = []
    # for address in obj:
    #     addresses.append(address.hartwell_address)

    # families = len(set(addresses))
     
    context = {
        'obj': obj,
        'date_printed': datetime.date.today(),
        }# class CreateRolesEntry(forms.ModelForm):1
#     class Meta:
#         model = VolunteerRole
#         fields = '__all__'
        
    return render(request, 'roster.html', context)


@login_required
@permission_required("volunteer.add_volunteer",  raise_exception=True)
def create(response, template_name='create.html'):
    form = VolunteerEntryForm(response.POST)
    if response.method == "POST":

        if form.is_valid():
            form.save()
            # member_id=Membership.newmanager.get(last_name='')    form = VolunteerEntryForm()    
            return redirect ( 'home')
            # return redirect('/update/' + str(form.id) + '/')
        else:
            print("didn't pass is_valid")
    return render(response, "create.html", {"form": form})

@login_required(login_url='login')
def mailtest(request):

    #     files = ['/home/jim/personal/mfa/2023_MFA_Membership_Form.pdf']
    #     obj = Membership.newmanager.all().order_by( 'last_name', 'first_name')
    #     # obj = Membership.newmanager.filter(last_name='Barlow')
    #     for people in obj:
    #       duespaid = people.dues_paid_for_year == '2023'
    #       lastname = people.last_name
    #       firstname = people.first_name
    #       cellphone = people.cell_phone
    #       email = people.email
    #       otherphone = people.home_phone
    #       address = people.hartwell_address
    #       otheraddress = people.other_home_address
    #       emergencycontact = people.emergency_contact_name
    #       emergencycontactphone = people.emergency_contact_phone
    #       context = ({
    #         'duespaid': duespaid,
    #         'lastname': lastname,
    #         'firstname': firstname,
    #         'cellphone': cellphone,
    #         'email': email,
    #         'otherphone': otherphone,    print(volunteer)
    print(volunteer.id)
    print(volunteer_id)
    #         'address': address,
    #         'otheraddress': otheraddress,
    #         'emergencycontact': emergencycontact
    #         'emergencycontactphone': emergencycontactphone
    #       })return HttpResponse('This was the email test')
    families = len(set(obj)) 

    return HttpResponse('This was the email test')


# @login_required(login_url='login')
# def create(response):
#     if response.method == "POST":
#         form = VolunteerEntryForm(response.POST)
#         if form.is_valid():
#             form.save()
#             # member_id=Membership.newmanager.get(last_name='')
#             return redirect ( 'home')    
         
#             # return redirect('/update/' + str(form.id) + '/')
#         else:
#             print("didn't pass is_valid")
#     form = VolunteerEntryForm()
#     return render(response, "create.html", {"form": form})

@login_required(login_url='login')
def update(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    form = VolunteerEntryForm(request.POST or None, 
        request.FILES or None, instance=volunteer)    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return redirect ('home')
            return redirect('/update/' + str(volunteer.id) + '/')
        else:
            print('form was not valid')

    print('Request was not a POST')
    return render(request, 'update.html',
                {'volunteer': volunteer,
                   'form': form})


@login_required(login_url='login')
@permission_required("volunteer.add_volunteer",  raise_exception=True)
def define_roles_catalog(request):
    if request.method == "POST":
        form = VolunteerRolesCatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('define_roles')
        else:
            print('roles form was not valid')
    form = VolunteerRolesCatalogForm()
    print('Request was not a POST')
    return render(request, 'create_roles.html', {"form": form})


@login_required(login_url='login')
def update_roles_catalog(request, role_id):
    role = VolunteerRolesCatalog.objects.get(pk=role_id)
    form = VolunteerRolesCatalogForm(
        request.POST or None, request.FILES or None, instance=role)
  
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return redirect('/update_roles_catalog/' + str(role.id) + '/')
        else:
            print('form was not valid')

    return render(request, 'update_roles_catalog.html',
                {'role': role,
                'form': form})   

@login_required(login_url='login')
def delete_role(request, role_id):
    role = VolunteerRolesCatalog.objects.get(pk=role_id)

    role.delete()

    return redirect('/print_roles_catalog/')
@user_passes_test(lambda user: user.is_staff )
 

@login_required(login_url='login')
def print_roles_catalog(request):
    obj = VolunteerRolesCatalog.objects.all()
    context = {
        'obj': obj,
        'date_printed': datetime.date.today(),
        }
    return render(request, 'roles_catalog.html', context)

def about_us(request):
    return render ( request, 'about_us.html')


# def roster_by_role(request):
#     list_of_roles = VolunteerRolesCatalog.objects.all()
#     # vr = VolunteerRolesCatalog.objects.get(vol_role_catalog = "Board Member")
#     # print (vr.id)
#     # print (vr.vol_role_catalog)
#     # print (vr.volunteer_role_catalog_description)
#     # outer loop, role by role

   

#     # for role in list_of_roles:
    
#     #     print (role.vol_role_catalog)
#     #     obj = vr.volunteer
    
        
#     context = {
#         'list_of_roles': list_of_roles,
#         # 'obj': obj,
#         'date_printed': datetime.date.today(),
#     }
#     return render (request, "roster_by_role.html", context)

    
    return redirect('print_roles_catalog')

    

    