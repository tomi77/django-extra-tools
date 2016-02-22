import unittest
try:
    from unittest import mock
except ImportError:
    import mock

from django_extras.db import pg_version


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


class PgVersionTestCase(unittest.TestCase):
    @mock.patch('t77_django.db.get_connection', mock_get_connection('9.4.1'))
    def test_9_4_1(self):
        """Version 9.4.1"""
        self.assertEqual(pg_version(), (9, 4, 1))

    @mock.patch('t77_django.db.get_connection', mock_get_connection('9.1.2'))
    def test_9_1_2(self):
        """Version 9.1.2"""
        self.assertEqual(pg_version(), (9, 1, 2))
