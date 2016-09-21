==================
django-extra-tools
==================

.. image:: https://travis-ci.org/tomi77/django-extra-tools.svg?branch=master
   :target: https://travis-ci.org/tomi77/django-extra-tools
.. image:: https://coveralls.io/repos/github/tomi77/django-extra-tools/badge.svg
   :target: https://coveralls.io/github/tomi77/django-extra-tools?branch=master
.. image:: https://codeclimate.com/github/tomi77/django-extra-tools/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-extra-tools
   :alt: Code Climate

Installation
============

.. sourcecode:: sh

   pip install django-extra-tools

Quick start
===========

Enable ``django-extra-tools``

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django_extra_tools',
   ]

Install SQL functions

.. sourcecode:: sh

   python manage.py migrate

StringAgg aggregate function on Django 1.4 needs monkey patch

.. sourcecode:: python

   from django_extra_tools.monkey import patch_django

   patch_all()

Template filters
================

parse_datetime
--------------

Parse datetime from string.

.. sourcecode:: htmldjango

   {% load parse %}

   {{ string_datetime|parse_datetime|date:"Y-m-d H:i" }}

parse_date
----------

Parse date from string.

.. sourcecode:: htmldjango

   {% load parse %}

   {{ string_date|parse_date|date:"Y-m-d" }}

parse_time
----------

Parse time from string.

.. sourcecode:: htmldjango

   {% load parse %}

   {{ string_time|parse_time|date:"H:i" }}

parse_duration
--------------

Parse duration (timedelta) from string.

.. sourcecode:: htmldjango

   {% load parse %}

   {{ string_duration|parse_duration }}

Aggregation
===========

First
-----

Returns the first non-NULL item.

.. sourcecode:: python

   from django_extra_tools.db.models.aggregates import First

   Table.objects.aggregate(First('col1', order_by='col2'))

Last
----

Returns the last non-NULL item.

.. sourcecode:: python

   from django_extra_tools.db.models.aggregates import Last

   Table.objects.aggregate(Last('col1', order_by='col2'))

Median
------

Returns median value.

.. sourcecode:: python

   from django_extra_tools.db.models.aggregates import Median

   Table.objects.aggregate(Median('col1'))

StringAgg
---------

Combines the values as the text. Fields are separated by a "separator".

.. sourcecode:: python

   from django_extra_tools.db.models.aggregates import StringAgg

   Table.objects.aggregate(StringAgg('col1'))

Database functions
==================

batch_qs
--------

Returns a (start, end, total, queryset) tuple for each batch in the given queryset.

.. sourcecode:: python

   from django_extra_tools.db.models import batch_qs

   qs = Table.objects.all()
   start, end, total, queryset = batch_qs(qs, 10)

pg_version
----------

Return tuple with PostgreSQL version of a specific connection.

.. sourcecode:: python

   from django_extra_tools.db.models import pg_version

   version = pg_version()

HTTP Response
=============

HttpResponseGetFile
-------------------

An HTTP response class with the "download file" headers.

.. sourcecode:: python

   from django_extra_tools.http import HttpResponseGetFile

   return HttpResponseGetFile(filename='file.txt', content=b'file content', content_type='file/text')

WSGI Request
============

get_client_ip
-------------

Get the client IP from the request.

.. sourcecode:: python

   from django_extra_tools.wsgi_request import get_client_ip

   ip = get_client_ip(request)

Management
==========

OneInstanceCommand
------------------

A management command which will be run only one instance of command with
name ``name``. No other command with name ``name`` can not be run in the
same time.

.. sourcecode:: python

   from django_extra_tools.management import OneInstanceCommand

   class MyCommand(OneInstanceCommand):
       name = 'mycommand'

       def handle_instance(self, *args, **kwargs):
           # some operations

