from django.db.transaction import get_connection


def pg_version(using=None):
    """
    Return tuple with PostgreSQL version of a specific connection
    :type using: str
    :param using: Connection name
    :rtype: tuple
    :return: PostgreSQL version
    """
    connection = get_connection(using)
    cursor = connection.cursor()

    cursor.execute('SHOW server_version')
    row = cursor.fetchone()

    return tuple([int(i) for i in row[0].split('.')])
