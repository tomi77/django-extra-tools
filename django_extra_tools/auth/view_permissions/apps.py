from django.apps import AppConfig

from .signals import add_view_permissions

try:
    from django.db.models.signals import post_syncdb
except ImportError:
    post_syncdb = None

try:
    from django.db.models.signals import post_migrate
except ImportError:
    post_migrate = None


class ViewPermissionsConfig(AppConfig):
    name = 'django_extra_tools.auth.view_permissions'
    verbose_name = 'View permissions'

    def ready(self):
        if post_syncdb is not None:
            post_syncdb.connect(add_view_permissions, sender=self)
        if post_migrate is not None:
            post_migrate.connect(add_view_permissions, sender=self)
