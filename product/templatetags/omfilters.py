from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formated(val):
    return utils.price_formated(val)


@register.filter
def cart_total_qtd(val):
    return utils.cart_total_qtd(val)


@register.filter
def cart_totals(val):
    return utils.cart_totals(val)
