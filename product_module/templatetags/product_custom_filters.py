from django import template

register = template.Library()


@register.filter
def get_tooman(price):
    return   '{:,}'.format(price) + ' تومان '
