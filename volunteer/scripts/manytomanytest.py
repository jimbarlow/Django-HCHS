# from volunteer.views import *
from volunteer.models import VolunteerRolesCatalog, Volunteer
from django.db import connection


def run():
    
    # Scratch Pad Area


    # for i in VolunteerRolesCatalog.objects.all():
    #     print (i.vol_role_catalog)

    vol_role_catalog = "Board Member"
    vr = VolunteerRolesCatalog.objects.filter(vol_role_catalog)
    print (vr.id)
    print (vr.vol_role_catalog)
    print (vr.volunteer_role_catalog_description)

    # print (vr.volunteer_role.all())
    
    # for i in VolunteerRolesCatalog.objects.all():
    #     print (vr.vol_role_catalog)

    #     for j in vr.volunteer_role.all():
    #         print (j.last_name, j.first_name)
    # # in the above i is the volunteer.


    Volunteer.objects.filter(volunteer_role=5)
