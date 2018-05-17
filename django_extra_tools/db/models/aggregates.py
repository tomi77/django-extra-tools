"""
Classes to represent the definitions of aggregate functions.
"""
from django.db.models import Aggregate


class AggregateWithOrderBy(Aggregate):
    template = '%(function)s(%(expressions)s%(order_by)s)'

    def __init__(self, expression, order_by=None, **extra):
        order_by = order_by and ' ORDER BY %s' % order_by or ''
        super(AggregateWithOrderBy, self).__init__(expression,
                                                   order_by=order_by,
                                                   **extra)


class First(AggregateWithOrderBy):
    name = 'First'
    function = 'FIRST'


class Last(AggregateWithOrderBy):
    name = 'Last'
    function = 'LAST'


class Median(Aggregate):
    name = 'Median'
    function = 'MEDIAN'

    def convert_value(self, value, expression, connection, context):
        return value


class StringAgg(Aggregate):
    name = 'StringAgg'
    function = 'STRING_AGG'
    template = "%(function)s(%(expressions)s::TEXT, '%(delimiter)s')"

    def __init__(self, expression, delimiter=',', **extra):
        super(StringAgg, self).__init__(expression, delimiter=delimiter,
                                        **extra)

    def convert_value(self, value, expression, connection, context):
        return value
