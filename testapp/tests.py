from django.test import TestCase

from django_extras.db import pg_version
from django_extras.db.models.aggregates import First, Last
from testapp.models import FirstLastTest, MedianTest

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
    @mock.patch('django_extras.db.get_connection', mock_get_connection('9.4.1'))
    def test_9_4_1(self):
        """Version 9.4.1"""
        self.assertEqual(pg_version(), (9, 4, 1))

    @mock.patch('django_extras.db.get_connection', mock_get_connection('9.1.2'))
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
