from django import template

register = template.Library()


@register.filter
def changeUnderline(string):
    return string.replace('_', ' ')

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()