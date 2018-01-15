from django import template

register = template.Library()


@register.filter
def changeUnderline(string):
    return string.replace('_', ' ')


@register.filter
def changeSemicolumn(string):
    return string.replace(';', ', ')


@register.filter(name='split')
def split(value, key):
    return value.split(key)
