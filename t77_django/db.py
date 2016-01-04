from django.db import connection


def pg_version():
    """Return PostgreSQL version"""
    cursor = connection.cursor()

    cursor.execute('SHOW server_version')
    row = cursor.fetchone()

    return tuple([int(i) for i in row[0].split('.')])
