"""
Classes to represent the default SQL aggregate functions
"""
from django.db.models.fields import CharField
from django.db.models.sql.aggregates import Aggregate


class AggregateWithOrderBy(Aggregate):
    sql_template = '%(function)s(%(field)s%(order_by)s)'


class First(AggregateWithOrderBy):
    sql_function = 'first'


class Last(AggregateWithOrderBy):
    sql_function = 'last'


class Median(Aggregate):
    sql_function = 'median'
    is_computed = True


class StringAgg(Aggregate):
    sql_function = 'string_agg'
    sql_template = "%(function)s(%(field)s::TEXT, '%(delimiter)s')"

    def __init__(self, col, **extra):
        super(StringAgg, self).__init__(col, **extra)

        self.field = CharField()
