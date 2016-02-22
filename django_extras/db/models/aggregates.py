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


class Last(Aggregate):
    name = 'Last'


class Median(Aggregate):
    name = 'Median'


class StringAgg(Aggregate):
    name = 'StringAgg'
