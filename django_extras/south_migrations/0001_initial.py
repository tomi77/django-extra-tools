import os

from south.db import db
from south.v2 import SchemaMigration

SQL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
FIRST_SQL = open(os.path.join(SQL_PATH, 'first.sql')).read()
LAST_SQL = open(os.path.join(SQL_PATH, 'last.sql')).read()
MEDIAN_SQL = open(os.path.join(SQL_PATH, 'median.sql')).read()


class Migration(SchemaMigration):
    def forwards(self, orm):
        db.execute(FIRST_SQL)
        db.execute(LAST_SQL)
        db.execute(MEDIAN_SQL)
