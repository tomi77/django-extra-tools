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
::

   pip install django-extras

Quick start
===========

Enable ``django-extras``
::

   INSTALLED_APPS = [
       ...
       'django_extras',
   ]

Install SQL functions
::

   python manage.py migrate

StringAgg aggregate function on Django 1.4 needs monkey patch
::

   from django_extras.monkey import patch_django

   patch_all()
