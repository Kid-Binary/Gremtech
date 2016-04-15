from datetime import datetime

from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import activate, get_language

register = template.Library()


@register.filter
def interpolate_with_timeline(value, start_year):
    current_year = str(datetime.now().year)

    if start_year != current_year:
        timeline = ''.join([start_year, ' - ', current_year])
    else:
        timeline = current_year

    return value % timeline


@register.simple_tag
def get_url_with_kwargs(request):
    url_name = ''.join([
        request.resolver_match.app_name,
        ':',
        request.resolver_match.url_name,
    ])

    url_kwargs = request.resolver_match.kwargs

    return reverse(url_name, None, None, url_kwargs)
