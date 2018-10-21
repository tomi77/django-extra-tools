from django.db import models
from django.db.models import fields

from django_extra_tools.db.models import timestampable

permissions = (('view_x', 'Can view tests.X'),
               ('view_y', 'Can view tests.Y'),
               )


class FirstLastTest(models.Model):
    ts = fields.DateField()
    val = fields.IntegerField()


class MedianTest(models.Model):
    val_int = fields.IntegerField()
    val_float = fields.FloatField()


class StringAggTest(models.Model):
    val_str = fields.CharField(max_length=10)
    val_int = fields.IntegerField()


class TimestampableTest(timestampable.CreatedMixin, timestampable.UpdatedMixin,
                        timestampable.DeletedMixin, models.Model):
    name = models.CharField(max_length=10)
