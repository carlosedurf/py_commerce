from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formated(val):
    return utils.price_formated(val)
