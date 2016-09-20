from django.template import Library
from django.utils.dateparse import parse_date

register = Library()


@register.filter('parse_date', expects_localtime=True)
def parse_date_filter(value):
    return parse_date(value)
