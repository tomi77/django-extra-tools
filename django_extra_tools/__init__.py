from .auth.permissions import add_view_permissions
from .conf import settings

try:
    from django.db.models.signals import post_syncdb
except ImportError:
    post_syncdb = None

try:
    from django.db.models.signals import post_migrate
except ImportError:
    post_migrate = None

if settings.CREATE_VIEW_PERMISSIONS:
    if post_syncdb is not None:
        post_syncdb.connect(add_view_permissions)
    if post_migrate is not None:
        post_migrate.connect(add_view_permissions)
