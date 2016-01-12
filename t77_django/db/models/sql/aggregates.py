from django.db.models.aggregates import Aggregate


class First(Aggregate):
    sql_function = 'first'
    sql_template = '%(function)s(%(field)s%(order_by)s)'

    def __init__(self, col, order_by=None, **extra):
        super(First, self).__init__(col, order_by=order_by and ' ORDER BY %s' % order_by or '', **extra)


class Last(Aggregate):
    sql_function = 'last'
    sql_template = '%(function)s(%(field)s%(order_by)s)'

    def __init__(self, col, order_by=None, **extra):
        super(Last, self).__init__(col, order_by=order_by and ' ORDER BY %s' % order_by or '', **extra)


class Median(Aggregate):
    sql_function = 'median'
    is_ordinal = True


class StringAgg(Aggregate):
    sql_function = 'string_agg'
    sql_template = "%(function)s(%(field)s, '%(delimiter)s')"

    def __init__(self, col, delimiter=',', **extra):
        super(StringAgg, self).__init__(col, delimiter="'%s'" % delimiter, **extra)
