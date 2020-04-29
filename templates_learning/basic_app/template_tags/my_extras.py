from djando import template

register = template.library()

@register.filter('cut')
def cut(value, arg):
    """
    This cuts out all values of arg from the str
    """
    return value.replace(arg, '')

