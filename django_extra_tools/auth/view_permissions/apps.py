from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .signals import add_view_permissions


class ViewPermissionsConfig(AppConfig):
    name = 'django_extra_tools.auth.view_permissions'
    verbose_name = 'View permissions'

    def ready(self):
        post_migrate.connect(add_view_permissions, sender=self)
