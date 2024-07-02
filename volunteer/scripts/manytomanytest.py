from volunteer.views import *
from volunteer.models import VolunteerRolesCatalog

def run():
    
    # Scratch Pad Area


    for i in VolunteerRolesCatalog.objects.all():
        print (i.vol_role_catalog)


    vr = VolunteerRolesCatalog.objects.get(vol_role_catalog = "Board Member")
    print (vr.id)
    print (vr.vol_role_catalog)
    print (vr.volunteer_role_catalog_description)
    for i in vr.volunteer_role.all():
        print (i.last_name)