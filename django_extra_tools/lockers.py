import atexit
import os
import tempfile
from importlib import import_module

from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured

from django_extra_tools.conf import settings


class LockError(Exception):
    pass


def get_locker_class(import_path=None):
    if import_path is None:
        import_path = settings.DEFAULT_LOCKER_CLASS
    try:
        module_path, class_name = import_path.rsplit('.', 1)
    except ValueError:
        raise ImproperlyConfigured("{} isn't a locker module.".format(import_path))
    try:
        module = import_module(module_path)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing locker module %s: "%s"' % (module_path, e))
    try:
        return getattr(module, class_name)
    except AttributeError:
        raise ImproperlyConfigured('Locker module "%s" does not define a "%s" class.' % (module_path, class_name))


class FileLocker(object):
    """
    Create a "{name}.lock" file in temp directory.
    """
    def __call__(self, name):
        filename = os.path.join(tempfile.gettempdir(), '{}.lock'.format(name))

        try:
            fd = os.open(filename, os.O_CREAT | os.O_EXCL)

            def register():
                os.close(fd)
                os.remove(filename)

            atexit.register(register)
        except OSError:
            msg = ("Script run multiple times. If this isn't true, delete "
                   "`%s`." % filename)
            raise LockError(msg)


class CacheLocker(object):
    """
    Create a "locker-{name}" key in cache.
    """
    def __call__(self, name):
        key = "locker-{}".format(name)

        if cache.get(key) is not None:
            msg = ("Script run multiple times. If this isn't true, delete "
                   "`%s` key." % key)
            raise LockError(msg)
        else:
            cache.set(key, os.getpid())

        def register():
            cache.delete(key)

        atexit.register(register)


lock = get_locker_class()
