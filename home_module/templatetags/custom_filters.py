from django import template

register = template.Library()

# this function return list[index % 3] because the template has three state for li class
@register.filter
def get_item(lst, index):
    return lst[index%3]