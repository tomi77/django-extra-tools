"""PostgreSQL Data Type Formatting Functions"""
from django.db.models import Func, DateField, DateTimeField, FloatField, TextField


class ToChar(Func):
    """
    Convert time stamp, interval, integer, real, double precision and
    numeric to string
    """
    function = 'TO_CHAR'
    output_field = TextField()


class ToDate(Func):
    """Convert string to date"""
    function = 'TO_DATE'
    output_field = DateField()


class ToNumber(Func):
    """Convert string to numeric"""
    function = 'TO_NUMBER'
    output_field = FloatField()


class ToTimestamp(Func):
    """Convert string to time stamp"""
    function = 'TO_TIMESTAMP'
    output_field = DateTimeField()
