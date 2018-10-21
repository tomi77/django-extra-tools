"""PostgreSQL Date/Time Functions"""
from django.db.models import Func, Value, DateField, DateTimeField, DurationField, FloatField, TimeField


class Age(Func):
    """
    Subtract arguments, producing a "symbolic" result that uses years and months, rather than just days.
    age(timestamp, timestamp)

    Subtract from current_date (at midnight).
    age(timestamp)
    """
    function = 'AGE'
    output_field = DurationField()


class ClockTimestamp(Func):
    """Current date and time (changes during statement execution)"""
    function = 'CLOCK_TIMESTAMP'
    template = '%(function)s()'
    output_field = DateTimeField()


class CurrentDate(Func):
    """Current date"""
    function = 'CURRENT_DATE'
    template = '%(function)s'
    output_field = DateField()


class CurrentTime(Func):
    """Current time of day"""
    function = 'CURRENT_TIME'
    template = '%(function)s'
    output_field = TimeField()


class CurrentTimestamp(Func):
    """Current date and time (start of current transaction)"""
    function = 'CURRENT_TIMESTAMP'
    template = '%(function)s'
    output_field = DateTimeField()


class DatePart(Func):
    """
    Get subfield (equivalent to extract)
    date_part(text, timestamp)
    date_part(text, interval)
    """
    function = "DATE_PART"
    output_field = FloatField()

    """
    The century
    The first century starts at 0001-01-01 00:00:00 AD, although they did not know
    it at the time. This definition applies to all Gregorian calendar countries.
    There is no century number 0, you go from -1 century to 1 century.
    """
    CENTURY = Value('century')

    """
    For timestamp values, the day (of the month) field (1 - 31).
    For interval values, the number of days.
    """
    DAY = Value('day')

    """The year field divided by 10"""
    DECADE = Value('decade')

    """The day of the week as Sunday (0) to Saturday (6)"""
    DAY_OF_WEEK = Value('dow')

    """The day of the year (1 - 365/366)"""
    DAY_OF_YEAR = Value('doy')

    """
    For timestamp with time zone values, the number of seconds since
    1970-01-01 00:00:00 UTC (can be negative).
    For date and timestamp values, the number of seconds since
    1970-01-01 00:00:00 local time.
    For interval values, the total number of seconds in the interval
    """
    EPOCH = Value('epoch')

    """The hour field (0 - 23)"""
    HOUR = Value('hour')

    """The day of the week as Monday (1) to Sunday (7)"""
    ISO_DAY_OF_WEEK = Value('isodow')

    """
    The ISO 8601 week-numbering year that the date falls in (not applicable to
    intervals).
    Each ISO 8601 week-numbering year begins with the Monday of the week
    containing the 4th of January, so in early January or late December the
    ISO year may be different from the Gregorian year. See the week field for
    more information.
    This field is not available in PostgreSQL releases prior to 8.3.
    """
    ISO_YEAR = Value('isoyear')

    """
    The seconds field, including fractional parts, multiplied by 1 000 000.
    Note that this includes full seconds
    """
    MICROSECONDS = Value('microseconds')

    """The millennium"""
    MILLENNIUM = Value('millennium')

    """
    The seconds field, including fractional parts, multiplied by 1000.
    Note that this includes full seconds.
    """
    MILLISECONDS = Value('milliseconds')

    """The minutes field (0 - 59)"""
    MINUTE = Value('minute')

    """
    For timestamp values, the number of the month within the year (1 - 12).
    For interval values, the number of months, modulo 12 (0 - 11)
    """
    MONTH = Value('month')

    """The quarter of the year (1 - 4) that the date is in"""
    QUARTER = Value('quarter')

    """The seconds field, including fractional parts (0 - 59)"""
    SECOND = Value('second')

    """
    The time zone offset from UTC, measured in seconds.
    Positive values correspond to time zones east of UTC,
    negative values to zones west of UTC.
    """
    TIMEZONE = Value('timezone')

    """The hour component of the time zone offset"""
    TIMEZONE_HOUR = Value('timezone_hour')

    """The minute component of the time zone offset"""
    TIMEZONE_MINUTE = Value('timezone_minute')

    """
    The number of the ISO 8601 week-numbering week of the year.
    By definition, ISO weeks start on Mondays and the first week of a year
    contains January 4 of that year. In other words, the first Thursday of
    a year is in week 1 of that year.

    In the ISO week-numbering system, it is possible for early-January dates
    to be part of the 52nd or 53rd week of the previous year, and for
    late-December dates to be part of the first week of the next year. For
    example, 2005-01-01 is part of the 53rd week of year 2004, and
    2006-01-01 is part of the 52nd week of year 2005, while 2012-12-31 is part
    of the first week of 2013. It's recommended to use the isoyear field
    together with week to get consistent results.
    """
    WEEK = Value('week')

    """
    The year field. Keep in mind there is no 0 AD, so subtracting BC years
    from AD years should be done with care.
    """
    YEAR = Value('year')


class DateTrunc(Func):
    """Truncate to specified precision"""
    function = "DATE_TRUNC"
    output_field = DateTimeField()

    MICROSECONDS = DatePart.MICROSECONDS
    MILLISECONDS = DatePart.MILLISECONDS
    SECOND = DatePart.SECOND
    MINUTE = DatePart.MINUTE
    HOUR = DatePart.HOUR
    DAY = DatePart.DAY
    WEEK = DatePart.WEEK
    MONTH = DatePart.MONTH
    QUARTER = DatePart.QUARTER
    YEAR = DatePart.YEAR
    DECADE = DatePart.DECADE
    CENTURY = DatePart.CENTURY
    MILLENNIUM = DatePart.MILLENNIUM
