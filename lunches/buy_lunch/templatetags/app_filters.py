from django import template
from buy_lunch.models import LUNCH_TYPE, APPETIZER_TYPE
register = template.Library()


@register.filter(name='lunch_type')
def lunch_type(value):
    return dict(LUNCH_TYPE).get(value)

@register.filter(name='appetizer_type')
def appetizer_type(value):
    return dict(APPETIZER_TYPE).get(value)