from django import template
from django.template.defaultfilters import stringfilter

from markdown_shortcodes import expand_shortcodes as expand_shortcodes_func

register = template.Library()

@register.filter
@stringfilter
def expand_shortcodes(val, extra_var=None):
    return expand_shortcodes_func(val, extra_var)
