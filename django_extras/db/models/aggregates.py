"""
Classes to represent the definitions of aggregate functions.
"""
from django.db.models import Aggregate as BaseAggregate

from .sql import aggregates as base_aggregates_module


class Aggregate(BaseAggregate):
    aggregates_module = base_aggregates_module

    def add_to_query(self, query, alias, col, source, is_summary):
        klass = getattr(self.aggregates_module, self.name)
        aggregate = klass(col, source=source, is_summary=is_summary,
                          **self.extra)
        query.aggregates[alias] = aggregate


class First(Aggregate):
    name = 'First'
    function = 'FIRST'
    template = '%(function)s(%(expressions)s%(order_by)s)'

    def __init__(self, expression, order_by=None, **extra):
        order_by = order_by and ' ORDER BY %s' % order_by or ''
        super(First, self).__init__(expression, order_by=order_by, **extra)


class Last(Aggregate):
    name = 'Last'
    function = 'LAST'
    template = '%(function)s(%(expressions)s%(order_by)s)'

    def __init__(self, expression, order_by=None, **extra):
        order_by = order_by and ' ORDER BY %s' % order_by or ''
        super(Last, self).__init__(expression, order_by=order_by, **extra)


class Median(Aggregate):
    name = 'Median'
    function = 'MEDIAN'


class StringAgg(Aggregate):
    name = 'StringAgg'
    function = 'STRINGAGG'
