# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-22 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_alter_timestampabletest'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionsTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.IntegerField()),
            ],
        ),
    ]
