from django import template

register = template.Library()


@register.filter
def changeUnderline(string):
    return string.replace('_', ' ')
