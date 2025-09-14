from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def cart_total(orders):
    total = 0
    for order in orders:
        total += order.quantity * order.product.price
    return total
