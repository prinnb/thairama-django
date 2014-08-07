from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cleanstring(value):
    return value.replace('Rice & Noodle $7.95', 'Rice_Noodle_7.95').replace(' ', '_').replace('Entree $7.95', 'Entree_7.95')