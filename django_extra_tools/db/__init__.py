try:
    from django.db.transaction import get_connection
except ImportError:
    from django.db import DEFAULT_DB_ALIAS, connections

    def get_connection(using=None):
        if using is None:
            using = DEFAULT_DB_ALIAS
        return connections[using]


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


def batch_qs(qs, batch_size=1000):
    """
    Returns a (start, end, total, queryset) tuple for each batch in the given
    queryset.

    Usage:
        # Make sure to order your queryset
        article_qs = Article.objects.order_by('id')
        for start, end, total, qs in batch_qs(article_qs):
            print "Now processing %s - %s of %s" % (start + 1, end, total)
            for article in qs:
                print article.body
    """
    total = qs.count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield (start, end, total, qs[start:end])
