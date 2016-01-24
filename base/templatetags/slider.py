from base.models import Slider
from django import template

register = template.Library()

@register.simple_tag()
def slider():
    items  =  Slider.objects.all()
    return items


