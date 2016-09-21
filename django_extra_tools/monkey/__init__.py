from __future__ import absolute_import

from django import VERSION


def patch_django():
    from django.db.backends.postgresql_psycopg2.operations import DatabaseOperations
    from .django import convert_values

    if VERSION[:2] == (1, 4):
        setattr(DatabaseOperations, 'convert_values', convert_values)
