from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cleanstring(value):
    return value.replace('Rice & Noodle $7.95', 'Rice_Noodle_795').replace('Entree $7.95', 'Entree_795').replace(' ', '_')