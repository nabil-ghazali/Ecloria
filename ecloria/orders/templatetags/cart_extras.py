# orders/templatetags/cart_extras.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplie deux valeurs"""
    try:
        return float(value) * int(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def calc_cart_total(orders):
    """Calcule le total du panier"""
    return sum(order.product.price * order.quantity for order in orders)
