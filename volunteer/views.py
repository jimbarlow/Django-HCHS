from django.shortcuts import render, redirect, resolve_url
from django.db import models
from django.template.loader import get_template
from django.template import Template, Context
from .models import Volunteers
from django.urls import reverse
# Datetime stuff
import datetime
from django.http import HttpResponse
# from collections import Counter
from .forms import CreateVolunteersEntry, UpdateVolunteersEntry
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
import os
# import pprint
# from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# for class based views:
from django.views import View
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
# from .forms import MemberShipYearsForm
# for Formtools multi form wizardry
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail, get_connection
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

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
#         return HttpResponseRedirect('home')

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

   
@login_required
def browse_roster(request):

    obj = Volunteers.objects.all().order_by('last_name','first_name')

    # addresses = []
    # for address in obj:
    #     addresses.append(address.hartwell_address)

    # families = len(set(addresses))
     
    context = {
        'obj': obj,
        'date_printed': datetime.date.today(),
        }

    return render(request, 'roster.html', context)

@login_required
def csv( request, year2view ):
    print ( year2view )
    print(type( year2view ))
    end_year2view=str(int(year2view)+1)
    print (end_year2view)
    print(type(end_year2view))
    obj = Membership.newmanager.all().filter(membershipyears__year__gte=datetime.date(int(year2view), 1, 1 )).filter(membershipyears__year__lt=datetime.date(int(end_year2view),1,1)).order_by('last_name','first_name').distinct()

    output_file_name = datetime.datetime.now().strftime("MFA-CSV %Y%m%d-%H.csv")
    # print
    with open(output_file_name, 'w') as csvfile:
      print (os.curdir)
      cwd = os.getcwd()
      print(cwd)
      print(os.listdir())
      # print("Changing one directory up")
      # os.chdir("..")
      # print(os.listdir())
      # #  os.chdir("/static")
      # # cwd = os.getcwd()
      # print(cwd)

      for i in obj:
          csvfile.write(i.first_name +' '+ i.last_name +',' +i.email+','+ i.cell_phone + '\n')
          print(i.first_name +' '+ i.last_name +',' +i.email+','+ i.cell_phone)

      print("Let's see if we can find the output file")
      print(os.listdir())

          # print(i.first_name +' '+ i.last_name +',' +i.email+','+ i.cell_phone)
    
    # <a href="{{ your_file_url}}" download>

    print('now we return the response')
    
    # f = open(csvfile, "r")
    f = open(output_file_name, "r")
    return HttpResponse( f, headers={
       'Content-Type': 'application/vnd.ms-excel',
       'Content-Disposition': 'attachment; filename=mfa_evite_address_file.csv',
       # 'Content-Disposition': 'attachment; filename={{ output_file_name }}',
    })
# '<a href="{{ csvfile }}" download>')


@login_required
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
    #         'otherphone': otherphone,
    #         'address': address,
    #         'otheraddress': otheraddress,
    #         'emergencycontact': emergencycontact
    #         'emergencycontactphone': emergencycontactphone
    #       })return HttpResponse('This was the email test')
    families = len(set(obj))

    return HttpResponse('This was the email test')


@login_required
def create(response):
    if response.method == "POST":
        form = CreateVolunteersEntry(response.POST)
        if form.is_valid():
            form.save()
            # member_id=Membership.newmanager.get(last_name='')
            return redirect ( 'home')
            # return redirect('/update/' + str(form.id) + '/')
        else:
            print("didn't pass is_valid")
    form = CreateVolunteersEntry()
    return render(response, "create.html", {"form": form})

@login_required
def update(request, volunteer_id):
    print('Update was called')
    volunteer = Volunteers.objects.get(pk=volunteer_id)
    print(volunteer)
    print(volunteer.id)
    print(volunteer_id)
    form = UpdateVolunteersEntry(
        request.POST or None, request.FILES or None, instance=volunteer)
    if request.method == 'POST':
        print('Call was an HCHS POST')

        if form.is_valid():
            print('Form was Valid')

            form.save()
            return redirect('/update/' + str(volunteer.id) + '/')
            # return redirect('/browse_roster/')
        else:
            print('form was not valid')

    print('Request was not a POST')
    return render(request, 'update.html',
                {'volunteer': volunteer,
                   'form': form})


