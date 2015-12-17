from django import template
from django.contrib.auth.models import User
from base.models import BasketProduct

register = template.Library()

@register.simple_tag(takes_context=True)
def basket_info(context):
    return 0
    uid = context['request'].user['user_id']
    return BasketProduct.objects.filter(user=uid).count()
