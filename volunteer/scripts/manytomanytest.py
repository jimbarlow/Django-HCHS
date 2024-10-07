# from volunteer.views import *
from volunteer.models import VolunteerRolesCatalog, Volunteer
from django.db import connection
from django.db.models import Q


def run():

    # replace this with a context building set    
    obj_role = VolunteerRolesCatalog.objects.all()
    obj_vol = Volunteer.objects.all()
    no_role_volenteer = Volunteer.objects.all().filter(volunteer_role=None)

    # context =  {
    #     'obj_role': obj_role,
    #     'obj_vol': obj_vol
    # }
    # end context building setup

    # context = {}
    # for j in obj_role:    

    #     # context[j.vol_role_catalog.lower()] = context.get(j.vol_role_catalog.lower(), []) + [j]
    #     context[j.vol_role_catalog] = context.get(j.vol_role_catalog, []) + [j]   
    # print (context)

    # query = "VolunteerRolesCatalog.objects.exclude("
    # for x in context:
    #     query = query + 'Q(vol_role_catalog = ' + "'" + str(x) + "') | "
    #     #query = query + 'dict' + '[' + str(x) +'], '
    # query = query + ')'

    # print (VolunteerRolesCatalog.objects.exclude(Q(vol_role_catalog = 'Board Member' ) | Q(vol_role_catalog = 'Kennel Assistant' )))

    # print (query)

    # query

    # query2 = VolunteerRolesCatalog.objects.exclude(Q(vol_role_catalog = 'Cat Volunteer Hartwell') | Q(vol_role_catalog = 'Board Member') | Q(vol_role_catalog = 'Kennel Assistant') | Q(vol_role_catalog = 'Fund Raising') | Q(vol_role_catalog = 'Cat Herder') | Q(vol_role_catalog = 'Dog Foster') | Q(vol_role_catalog = 'Pooper Picker Upper Supreme')

# ingredients in ingredients category

#ingrcat --|          volunteer_roles --|
#          |                            |
#        ingredients                volunteers