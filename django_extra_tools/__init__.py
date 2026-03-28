import django

if django.VERSION < (4, 0):
    default_app_config = 'django_extra_tools.apps.DjangoExtraToolsConfig'
