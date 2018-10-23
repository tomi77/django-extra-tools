"""PostgreSQL Data Type Formatting Functions"""
from django.db.models import Func, DateField, DateTimeField, FloatField, TextField, Value


class ToChar(Func):
    """
    Convert time stamp, interval, integer, real, double precision and
    numeric to string
    """
    function = 'TO_CHAR'
    output_field = TextField()

    def __init__(self, expression, pattern, **extra):
        if not hasattr(pattern, 'resolve_expression'):
            pattern = Value(pattern)
        super(ToChar, self).__init__(expression, pattern, **extra)


class ToDate(Func):
    """Convert string to date"""
    function = 'TO_DATE'
    output_field = DateField()

    def __init__(self, expression, pattern, **extra):
        if not hasattr(pattern, 'resolve_expression'):
            pattern = Value(pattern)
        super(ToDate, self).__init__(expression, pattern, **extra)


class ToNumber(Func):
    """Convert string to numeric"""
    function = 'TO_NUMBER'
    output_field = FloatField()

    def __init__(self, expression, pattern, **extra):
        if not hasattr(pattern, 'resolve_expression'):
            pattern = Value(pattern)
        super(ToNumber, self).__init__(expression, pattern, **extra)


class ToTimestamp(Func):
    """Convert string to time stamp"""
    function = 'TO_TIMESTAMP'
    output_field = DateTimeField()

    def __init__(self, expression, pattern=None, **extra):
        expressions = [expression]
        if pattern is not None:
            if not hasattr(pattern, 'resolve_expression'):
                pattern = Value(pattern)
            expressions.append(pattern)
        super(ToTimestamp, self).__init__(*expressions, **extra)
