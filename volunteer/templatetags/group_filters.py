from django import template
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    print(user)
    print(group_name)
    try:
        print (user.groups)
        return user.groups.filter(name=group_name).exists()
    except:
        print('did not work')
