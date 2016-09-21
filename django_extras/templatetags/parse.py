from django.template import Library
from django.utils.dateparse import parse_date, parse_datetime, parse_time, parse_duration

register = Library()


@register.filter('parse_datetime', expects_localtime=True)
def parse_datetime_filter(value):
    return parse_datetime(value)


@register.filter('parse_date', expects_localtime=True)
def parse_date_filter(value):
    return parse_date(value)


@register.filter('parse_time', expects_localtime=True)
def parse_time_filter(value):
    return parse_time(value)


@register.filter('parse_duration')
def parse_duration_filter(value):
    return parse_duration(value)
