from django import template
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        return user.groups.filter(name=group_name).exists()
    except:
        print('did not work')
        return False

@register.filter(name='get_range')
def get_range(value):
    return range(value)
