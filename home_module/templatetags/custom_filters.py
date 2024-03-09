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




