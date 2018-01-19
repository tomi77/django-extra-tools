from __future__ import print_function

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


def add_view_permissions(sender, verbosity, **kwargs):
    """
    This post_syncdb/post_migrate hooks takes care of adding a view permission too all our
    content types.
    """
    for content_type in ContentType.objects.all():
        codename = "view_%s" % content_type.model

        _, created = Permission.objects \
            .get_or_create(content_type=content_type,
                           codename=codename,
                           defaults={'name': 'Can view %s' % content_type.name})
        if created and verbosity >= 1:
            print('Added view permission for %s' % content_type.name)
