# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FirstLastTest'
        db.create_table('tests_firstlasttest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts', self.gf('django.db.models.fields.DateField')()),
            ('val', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tests', ['FirstLastTest'])

        # Adding model 'MedianTest'
        db.create_table('tests_mediantest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('val_int', self.gf('django.db.models.fields.IntegerField')()),
            ('val_float', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tests', ['MedianTest'])

        # Adding model 'StringAggTest'
        db.create_table('tests_stringaggtest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('val_str', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('val_int', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tests', ['StringAggTest'])

        # Adding model 'TimestampableTest'
        db.create_table('tests_timestampabletest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tests_timestampabletest_created', blank=True, db_column=u'created_by', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'tests_timestampabletest_updated', null=True, db_column=u'updated_by', to=orm['auth.User'])),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deleted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'tests_timestampabletest_deleted', null=True, db_column=u'deleted_by', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('tests', ['TimestampableTest'])


    def backwards(self, orm):
        # Deleting model 'FirstLastTest'
        db.delete_table('tests_firstlasttest')

        # Deleting model 'MedianTest'
        db.delete_table('tests_mediantest')

        # Deleting model 'StringAggTest'
        db.delete_table('tests_stringaggtest')

        # Deleting model 'TimestampableTest'
        db.delete_table('tests_timestampabletest')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tests.firstlasttest': {
            'Meta': {'object_name': 'FirstLastTest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ts': ('django.db.models.fields.DateField', [], {}),
            'val': ('django.db.models.fields.IntegerField', [], {})
        },
        'tests.mediantest': {
            'Meta': {'object_name': 'MedianTest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val_float': ('django.db.models.fields.FloatField', [], {}),
            'val_int': ('django.db.models.fields.IntegerField', [], {})
        },
        'tests.stringaggtest': {
            'Meta': {'object_name': 'StringAggTest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val_int': ('django.db.models.fields.IntegerField', [], {}),
            'val_str': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'tests.timestampabletest': {
            'Meta': {'object_name': 'TimestampableTest'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tests_timestampabletest_created'", 'blank': 'True', 'db_column': "u'created_by'", 'to': "orm['auth.User']"}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'tests_timestampabletest_deleted'", 'null': 'True', 'db_column': "u'deleted_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'tests_timestampabletest_updated'", 'null': 'True', 'db_column': "u'updated_by'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['tests']