"""A set of timestampable model mixins"""
from __future__ import unicode_literals

import django
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class CreatedAtMixin(models.Model):
    """Add ``created_at`` field to model."""
    created_at = models.DateTimeField(auto_now_add=True,
                                      null=False, blank=True,
                                      verbose_name=_('Creation date'))

    class Meta(object):
        abstract = True


class CreatedByMixin(models.Model):
    """Add ``created_by`` field to model."""
    created_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),  # Django 1.4 hack
        db_column='created_by',
        null=False, blank=True,
        related_name='%(app_label)s_%(class)s_created',
        verbose_name=_('Created by'))

    class Meta(object):
        abstract = True


class UpdatedAtMixin(models.Model):
    """Add ``updated_at`` field to model."""
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True,
                                      verbose_name=_('Date of last update'))

    class Meta(object):
        abstract = True


class UpdatedByMixin(models.Model):
    """Add ``updated_by`` field to model."""
    updated_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),  # Django 1.4 hack
        db_column='updated_by',
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_updated',
        verbose_name=_('Updated by'))

    class Meta(object):
        abstract = True

    def save_by(self, user, force_insert=False, force_update=False, using=None,
                update_fields=None):
        self.updated_by = user
        if django.VERSION[:2] > (1, 4):
            return self.save(force_insert, force_update, using, update_fields)
        else:
            return self.save(force_insert, force_update, using)


class DeletedAtMixin(models.Model):
    """Add ``deleted_at`` field to model."""
    deleted_at = models.DateTimeField(null=True, blank=True,
                                      verbose_name=_('Removal date'))

    class Meta(object):
        abstract = True

    def delete(self, using=None):
        self.deleted_at = timezone.now()
        self.save()


class DeletedByMixin(models.Model):
    """Add ``deleted_by`` field to model."""
    deleted_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),  # Django 1.4 hack
        db_column='deleted_by',
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_deleted',
        verbose_name=_('Deleted by'))

    class Meta(object):
        abstract = True

    def delete(self, using=None):
        pass

    def delete_by(self, user, using=None):
        self.deleted_by = user
        self.delete(using)


class CreatedMixin(CreatedAtMixin, CreatedByMixin):
    """Add ``created_at`` and ``created_by`` fields to model."""
    class Meta(object):
        abstract = True


class UpdatedMixin(UpdatedAtMixin, UpdatedByMixin):
    """Add ``updated_at`` and ``updated_by`` fields to model."""
    class Meta(object):
        abstract = True


class DeletedMixin(DeletedAtMixin, DeletedByMixin):
    """Add ``deleted_at`` and ``deleted_by`` fields to model."""
    class Meta(object):
        abstract = True
