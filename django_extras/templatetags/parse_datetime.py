from django.template import Library
from django.utils.dateparse import parse_datetime

register = Library()


@register.filter('parse_datetime', expects_localtime=True)
def parse_datetime_filter(value):
    return parse_datetime(value)
