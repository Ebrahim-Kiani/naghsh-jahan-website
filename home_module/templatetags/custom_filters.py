import jdatetime
from django import template

register = template.Library()

# this function return list[index % 3] because the template has three state for li class
@register.filter
def get_item(lst, index):
    return lst[index%3]
@register.filter
def number_of_pairs(lst):
    return range(int(len(lst) / 2))

@register.filter
def get_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

@register.filter
def gregorian_to_shamsi(value):
    if value:
        shamsi_date = jdatetime.datetime.fromgregorian(datetime=value)
        return shamsi_date.strftime('%Y-%m-%d')
    return value


@register.filter
def positive_five(value):
    return value+5


