# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLastTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ts', models.DateField()),
                ('val', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedianTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val_int', models.IntegerField()),
                ('val_float', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StringAggTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val_str', models.CharField(max_length=10)),
                ('val_int', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimestampableTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last update date', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete date', blank=True)),
                ('name', models.CharField(max_length=10)),
                ('created_by', models.ForeignKey(related_name='testapp_timestampabletest_created', db_column='created_by', blank=True, to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(related_name='testapp_timestampabletest_deleted', db_column='deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='testapp_timestampabletest_updated', db_column='updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
