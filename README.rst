=============
django-extras
=============

.. image:: https://travis-ci.org/tomi77/django-extras.svg?branch=master
   :target: https://travis-ci.org/tomi77/django-extras
.. image:: https://coveralls.io/repos/github/tomi77/django-extras/badge.svg
   :target: https://coveralls.io/github/tomi77/django-extras?branch=master
.. image:: https://codeclimate.com/github/tomi77/django-extras/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-extras
   :alt: Code Climate

Installation
============

.. sourcecode:: sh

   pip install django-extras

Quick start
===========

Enable ``django-extras``

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django_extras',
   ]

Install SQL functions

.. sourcecode:: sh

   python manage.py migrate

StringAgg aggregate function on Django 1.4 needs monkey patch

.. sourcecode:: python

   from django_extras.monkey import patch_django

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

   from django_extras.db.models.aggregates import First

   Table.objects.aggregate(First('col1', order_by='col2'))

Last
----

Returns the last non-NULL item.

.. sourcecode:: python

   from django_extras.db.models.aggregates import Last

   Table.objects.aggregate(Last('col1', order_by='col2'))

Median
------

Returns median value.

.. sourcecode:: python

   from django_extras.db.models.aggregates import Median

   Table.objects.aggregate(Median('col1'))

StringAgg
---------

Combines the values as the text. Fields are separated by a "separator".

.. sourcecode:: python

   from django_extras.db.models.aggregates import StringAgg

   Table.objects.aggregate(StringAgg('col1'))

Database functions
==================

batch_qs
--------

Returns a (start, end, total, queryset) tuple for each batch in the given queryset.

.. sourcecode:: python

   from django_extras.db.models import batch_qs

   qs = Table.objects.all()
   start, end, total, queryset = batch_qs(qs, 10)

pg_version
----------

Return tuple with PostgreSQL version of a specific connection.

.. sourcecode:: python

   from django_extras.db.models import pg_version

   version = pg_version()

HTTP Response
=============

HttpResponseGetFile
-------------------

An HTTP response class with the "download file" headers.

.. sourcecode:: python

   from django_extras.http import HttpResponseGetFile

   return HttpResponseGetFile(filename='file.txt', content=b'file content', content_type='file/text')

WSGI Request
============

get_client_ip
-------------

Get the client IP from the request.

.. sourcecode:: python

   from django_extras.wsgi_request import get_client_ip

   ip = get_client_ip(request)

Management
==========

OneInstanceCommand
------------------

A management command which will be run only one instance of command with
name ``name``. No other command with name ``name`` can not be run in the
same time.

.. sourcecode:: python

   from django_extras.management import OneInstanceCommand

   class MyCommand(OneInstanceCommand):
       name = 'mycommand'

       def handle_instance(self, *args, **kwargs):
           # some operations

