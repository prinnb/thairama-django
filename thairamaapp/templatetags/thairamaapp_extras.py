from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cleanstring(value):
    return value.replace('$', '_').replace('&', '_').replace(' ', '_')