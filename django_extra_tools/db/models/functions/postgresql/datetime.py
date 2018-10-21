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


"""
The century
The first century starts at 0001-01-01 00:00:00 AD, although they did not know
it at the time. This definition applies to all Gregorian calendar countries.
There is no century number 0, you go from -1 century to 1 century.
"""
DATE_PART_CENTURY = Value('century')

"""
For timestamp values, the day (of the month) field (1 - 31).
For interval values, the number of days.
"""
DATE_PART_DAY = Value('day')

"""The year field divided by 10"""
DATE_PART_DECADE = Value('decade')

"""The day of the week as Sunday (0) to Saturday (6)"""
DATE_PART_DAY_OF_WEEK = Value('dow')

"""The day of the year (1 - 365/366)"""
DATE_PART_DAY_OF_YEAR = Value('doy')

"""
For timestamp with time zone values, the number of seconds since
1970-01-01 00:00:00 UTC (can be negative).
For date and timestamp values, the number of seconds since
1970-01-01 00:00:00 local time.
For interval values, the total number of seconds in the interval
"""
DATE_PART_EPOCH = Value('epoch')

"""The hour field (0 - 23)"""
DATE_PART_HOUR = Value('hour')

"""The day of the week as Monday (1) to Sunday (7)"""
DATE_PART_ISO_DAY_OF_WEEK = Value('isodow')

"""
The ISO 8601 week-numbering year that the date falls in (not applicable to
intervals).
Each ISO 8601 week-numbering year begins with the Monday of the week
containing the 4th of January, so in early January or late December the
ISO year may be different from the Gregorian year. See the week field for
more information.
This field is not available in PostgreSQL releases prior to 8.3.
"""
DATE_PART_ISO_YEAR = Value('isoyear')

"""
The seconds field, including fractional parts, multiplied by 1 000 000.
Note that this includes full seconds
"""
DATE_PART_MICROSECONDS = Value('microseconds')


class DatePart(Func):
    """
    Get subfield (equivalent to extract)
    date_part(text, timestamp)
    date_part(text, interval)
    """
    function = "DATE_PART"
    output_field = FloatField()
