from django.conf import settings as user_settings

from . import defaults


class AppSettings(object):
    def __getattr__(self, name):
        return getattr(user_settings, name, getattr(defaults, name))


settings = AppSettings()
