from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from django_extra_tools.db import pg_version
from django_extra_tools.db.models.aggregates import First, Last, Median, StringAgg
from django_extra_tools.templatetags.parse import parse_duration
from django_extra_tools.wsgi_request import get_client_ip
from testapp.models import FirstLastTest, MedianTest, StringAggTest

try:
    from unittest import mock
except ImportError:
    from mock import mock


def mock_get_connection(version):
    class MockCursor(object):
        def __init__(self, _version):
            self.version = _version

        def execute(self, *args):
            pass

        def fetchone(self):
            return [self.version]

    class MockConnection(object):
        def __init__(self, _version):
            self.version = _version

        def cursor(self):
            return MockCursor(self.version)

    def get_connection(using):
        return MockConnection(version)
    return get_connection


class PgVersionTestCase(TestCase):
    @mock.patch('django_extra_tools.db.get_connection', mock_get_connection('9.4.1'))
    def test_9_4_1(self):
        """Version 9.4.1"""
        self.assertEqual(pg_version(), (9, 4, 1))

    @mock.patch('django_extra_tools.db.get_connection', mock_get_connection('9.1.2'))
    def test_9_1_2(self):
        """Version 9.1.2"""
        self.assertEqual(pg_version(), (9, 1, 2))


class FirstTestCase(TestCase):
    fixtures = ['first_last.yaml']

    def test_first_with_order(self):
        qs = FirstLastTest.objects.all().aggregate(first=First('val', order_by='ts'))
        self.assertEqual(qs['first'], 10)


class LastTestCase(TestCase):
    fixtures = ['first_last.yaml']

    def test_last_with_order(self):
        qs = FirstLastTest.objects.all().aggregate(last=Last('val', order_by='ts'))
        self.assertEqual(qs['last'], 15)


class MedianTestCase(TestCase):
    fixtures = ['median.yaml']

    def test_odd_number_of_integers(self):
        qs = MedianTest.objects.all().aggregate(Median('val_int'))
        self.assertEqual(qs['val_int__median'], 15)

    def test_even_number_of_integers(self):
        qs = MedianTest.objects.filter(pk__lt=5).aggregate(Median('val_int'))
        self.assertEqual(qs['val_int__median'], 17.5)

    def test_odd_number_of_floats(self):
        qs = MedianTest.objects.all().aggregate(Median('val_float'))
        self.assertEqual(qs['val_float__median'], 15.0)

    def test_even_number_of_floats(self):
        qs = MedianTest.objects.filter(pk__lt=5).aggregate(Median('val_float'))
        self.assertEqual(qs['val_float__median'], 17.5)


class StringAggTestCase(TestCase):
    fixtures = ['string_agg.yaml']

    def test_default_delimiter(self):
        qs = StringAggTest.objects.all().aggregate(StringAgg('val_str'))
        self.assertEqual(qs['val_str__stringagg'], '1,2,3')

    def test_own_delimiter(self):
        qs = StringAggTest.objects.all().aggregate(StringAgg('val_str', delimiter='-'))
        self.assertEqual(qs['val_str__stringagg'], '1-2-3')

    def test_int_default_delimiter(self):
        qs = StringAggTest.objects.all().aggregate(StringAgg('val_int'))
        self.assertEqual(qs['val_int__stringagg'], '1,2,3')

    def test_int_own_delimiter(self):
        qs = StringAggTest.objects.all().aggregate(StringAgg('val_int', delimiter='-'))
        self.assertEqual(qs['val_int__stringagg'], '1-2-3')


class GetClientIpTestCase(TestCase):
    def test_empty_all(self):
        request = HttpRequest()
        self.assertIsNone(get_client_ip(request))

    def test_remote_addr(self):
        request = HttpRequest()
        request.META = {'REMOTE_ADDR': '10.10.0.1'}
        self.assertEqual(get_client_ip(request), '10.10.0.1')

    def test_x_forwarded_for(self):
        request = HttpRequest()
        request.META = {'HTTP_X_FORWARDED_FOR': '10.10.0.1'}
        self.assertIsNone(get_client_ip(request))

    def test_proxy(self):
        request = HttpRequest()
        request.META = {'REMOTE_ADDR': '192.168.0.1',
                        'HTTP_X_FORWARDED_FOR': '192.168.0.1,123.234.123.234'}
        self.assertEqual(get_client_ip(request), '123.234.123.234')


class ParseDateTestCase(TestCase):
    def test_parse_date(self):
        tpl = render_to_string('date.txt', {'datestr': '2016-01-02'})
        self.assertEqual(tpl, '2016-01-02')

    def test_incorrect_date(self):
        tpl = render_to_string('date.txt', {'datestr': 'not a date'})
        self.assertEqual(tpl, '')


class ParseDateTimeTestCase(TestCase):
    def test_parse_datetime(self):
        tpl = render_to_string('datetime.txt', {'datetimestr': '2016-01-02T12:23:34'})
        self.assertEqual(tpl, '2016-01-02 12:23:34')

    def test_incorrect_datetime(self):
        tpl = render_to_string('datetime.txt', {'datetimestr': 'not a datetime'})
        self.assertEqual(tpl, '')


class ParseTimeTestCase(TestCase):
    def test_parse_time(self):
        tpl = render_to_string('time.txt', {'timestr': '12:23:34'})
        self.assertEqual(tpl, '12:23:34')

    def test_incorrect_time(self):
        tpl = render_to_string('time.txt', {'timestr': 'not a time'})
        self.assertEqual(tpl, '')


if parse_duration is not None:
    class ParseDurationCase(TestCase):
        def test_parse_duration(self):
            tpl = render_to_string('duration.txt', {'durationstr': '12:23:34'})
            self.assertEqual(tpl, '12:23:34')

        def test_incorrect_duration(self):
            tpl = render_to_string('duration.txt', {'durationstr': 'not a duration'})
            self.assertEqual(tpl, 'None')
