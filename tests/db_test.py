import unittest
from unittest import mock

from t77_django.db import pg_version


class MockCursor(object):
    def __init__(self, version):
        self.version = version

    def execute(self, *args):
        pass

    def fetchone(self):
        return [self.version]


class MockConnection(object):
    def __init__(self, version):
        self.version = version

    def cursor(self):
        return MockCursor(self.version)


class PgVersionTestCase(unittest.TestCase):
    @mock.patch('t77_django.db.connection', MockConnection('9.4.1'))
    def test_9_4_1(self):
        """Version 9.4.1"""
        self.assertEqual(pg_version(), (9, 4, 1))

    @mock.patch('t77_django.db.connection', MockConnection('9.1.2'))
    def test_9_1_2(self):
        """Version 9.1.2"""
        self.assertEqual(pg_version(), (9, 1, 2))
