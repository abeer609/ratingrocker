from django import template

register = template.Library()

@register.filter(name='custom_range')
def custom_range(value):
    return range(value)

@register.filter(name='custom_range_with_value')
def custom_range_with_value(value, comparison_value):
    return range(value), comparison_value
