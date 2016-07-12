import os

from django.db import migrations

SQL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
FIRST_SQL = open(os.path.join(SQL_PATH, 'first.sql')).read()
LAST_SQL = open(os.path.join(SQL_PATH, 'last.sql')).read()
MEDIAN_SQL = open(os.path.join(SQL_PATH, 'median.sql')).read()


class Migration(migrations.Migration):
    operations = [
        migrations.RunSQL(FIRST_SQL),
        migrations.RunSQL(LAST_SQL),
        migrations.RunSQL(MEDIAN_SQL),
    ]
