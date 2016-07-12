from django.db import models
from django.db.models import fields


class FirstLastTest(models.Model):
    ts = fields.DateField()
    val = fields.IntegerField()
