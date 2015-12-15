from base.models import Category
from django import template

register = template.Library()

@register.simple_tag()
def category_menu():
    items  =  Category.objects.filter(parent__isnull=True)
    return items


