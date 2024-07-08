# from volunteer.views import *
from volunteer.models import VolunteerRolesCatalog, Volunteer
from django.db import connection


def run():

    # replace this with a context building set    
    obj_role = VolunteerRolesCatalog.objects.all()
    obj_vol = Volunteer.objects.all()
    


    context =  {
        'obj_role': obj_role,
        'obj_vol': obj_vol
    }
    # end context building setup

    for i in obj_role:    



        #context[i.volunteer_role.last_name()] = context.get(i.category.name.lower(), []) + [i]

        # newcontext = {'volunteers': volunteers, 'ingredients': ingredients, 'ingrcat': ingrcat, }

        # context = dict(context.items() + newcontext.items())

        print (i.vol_role_catalog, ' - ', i.volunteer_role_catalog_description)

        # These for loops move into Django Templating Language
        for j in VolunteerRolesCatalog.objects.filter(vol_role_catalog = i.vol_role_catalog):
             for item in j.volunteer_role.all():
                print ( item.first_name, item.last_name, item.cell_phone)



# ingredients in ingredients category

#ingrcat --|          volunteer_roles --|
#          |                            |
#        ingredients                volunteers