import os

import django


SECRET_KEY = 'qaz123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'travis'),
        'USER': os.environ.get('DATABASE_USER', 'travis'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django_extra_tools',
    'tests',
    'django_extra_tools.auth.view_permissions'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

MIDDLEWARE_CLASSES = [
    'django_extra_tools.middleware.XhrMiddleware'
]

if django.VERSION[:2] <= (1, 6):
    INSTALLED_APPS += ['south']
