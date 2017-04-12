"""
Classes to represent the definitions of aggregate functions.
"""
import django

if django.VERSION[:2] <= (1, 7):
    from django.db.models import Aggregate as BaseAggregate

    from .sql import aggregates as base_aggregates_module


    class Aggregate(BaseAggregate):
        aggregates_module = base_aggregates_module

        def add_to_query(self, query, alias, col, source, is_summary):
            klass = getattr(self.aggregates_module, self.name)
            aggregate = klass(col, source=source, is_summary=is_summary,
                              **self.extra)
            query.aggregates[alias] = aggregate
        pass
else:
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
