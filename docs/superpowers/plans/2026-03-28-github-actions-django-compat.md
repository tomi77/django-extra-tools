# GitHub Actions + Django Compatibility Plan

> **For Claude:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Zastąpić Travis CI przez GitHub Actions i naprawić kompatybilność kodu z Django 1.11, 2.2, 3.2 i 4.2.

**Architecture:** Każda poprawka kompatybilności jest niezależna i dotyczy konkretnego pliku. GitHub Actions workflow zastępuje `.travis.yml` z matrycą testów dla czterech wersji Django + PostgreSQL jako service.

**Tech Stack:** Django 1.11/2.2/3.2/4.2, Python 3.7/3.8/3.10/3.11, PostgreSQL, GitHub Actions

---

## Pliki do modyfikacji

- Utwórz: `.github/workflows/test.yml`
- Modyfikuj: `django_extra_tools/__init__.py` — usuń `default_app_config`
- Modyfikuj: `django_extra_tools/auth/view_permissions/__init__.py` — usuń `default_app_config`
- Modyfikuj: `django_extra_tools/auth/backends.py` — usuń gałąź dla Django < 1.11
- Modyfikuj: `django_extra_tools/db/models/aggregates.py` — napraw sygnaturę `convert_value()`
- Modyfikuj: `django_extra_tools/db/models/timestampable.py` — `ugettext_lazy` → `gettext_lazy`
- Modyfikuj: `django_extra_tools/middleware.py` — dodaj `MiddlewareMixin`
- Modyfikuj: `tests/settings.py` — `MIDDLEWARE_CLASSES` → `MIDDLEWARE`, dodaj `DEFAULT_AUTO_FIELD`
- Modyfikuj: `tests/tests.py` — usuń gałąź dla Django < 1.11
- Modyfikuj: `setup.py` — zaktualizuj klasyfikatory

---

### Task 1: GitHub Actions workflow

**Files:**
- Create: `.github/workflows/test.yml`

- [ ] **Krok 1: Utwórz katalog i plik workflow**

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: test_user
          POSTGRES_PASSWORD: test_pass
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    strategy:
      fail-fast: false
      matrix:
        include:
          - python-version: "3.7"
            django-version: "Django>=1.11,<2.0"
          - python-version: "3.8"
            django-version: "Django>=2.2,<3.0"
          - python-version: "3.10"
            django-version: "Django>=3.2,<4.0"
          - python-version: "3.11"
            django-version: "Django>=4.2,<5.0"

    env:
      DATABASE_NAME: test_db
      DATABASE_USER: test_user
      DATABASE_PASSWORD: test_pass
      DATABASE_HOST: 127.0.0.1
      DATABASE_PORT: 5432

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          pip install "${{ matrix.django-version }}" psycopg2-binary pyyaml coverage

      - name: Run migrations
        run: python manage.py migrate

      - name: Run tests
        run: coverage run manage.py test tests
```

- [ ] **Krok 2: Zweryfikuj poprawność YAML**

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/test.yml'))" && echo OK
```

---

### Task 2: Usuń `default_app_config` (Django 4.0+ usunął wsparcie)

**Files:**
- Modify: `django_extra_tools/__init__.py`
- Modify: `django_extra_tools/auth/view_permissions/__init__.py`

- [ ] **Krok 1: Wyczyść `django_extra_tools/__init__.py`**

Plik powinien być pusty (usunąć linię z `default_app_config`).

- [ ] **Krok 2: Wyczyść `django_extra_tools/auth/view_permissions/__init__.py`**

Plik powinien być pusty (usunąć linię z `default_app_config`).

---

### Task 3: Napraw `convert_value()` w aggregates.py

**Files:**
- Modify: `django_extra_tools/db/models/aggregates.py`

Django 2.1+ usunął parametr `context` z `convert_value()`. Użycie `*args` sprawia, że metoda akceptuje oba warianty.

- [ ] **Krok 1: Zaktualizuj sygnatury `convert_value`**

```python
# Median.convert_value:
def convert_value(self, value, expression, connection, *args, **kwargs):
    return value

# StringAgg.convert_value:
def convert_value(self, value, expression, connection, *args, **kwargs):
    return value
```

---

### Task 4: Napraw `ugettext_lazy` w timestampable.py

**Files:**
- Modify: `django_extra_tools/db/models/timestampable.py`

`ugettext_lazy` zostało usunięte w Django 4.0. `gettext_lazy` istnieje od Django 1.x.

- [ ] **Krok 1: Zmień import**

```python
# Stare:
from django.utils.translation import ugettext_lazy as _
# Nowe:
from django.utils.translation import gettext_lazy as _
```

- [ ] **Krok 2: Usuń też zbędny `from __future__ import unicode_literals`** (Python 2 only)

---

### Task 5: Zaktualizuj `XhrMiddleware`

**Files:**
- Modify: `django_extra_tools/middleware.py`

Old-style middleware (`process_request`/`process_response`) działa w Django 1.11-4.2 przez `MiddlewareMixin`. Dodanie `MiddlewareMixin` jest wzorcem zalecanym od Django 1.10.

- [ ] **Krok 1: Zaktualizuj klasę**

```python
from django import http
from django.utils.deprecation import MiddlewareMixin

from django_extra_tools.conf import settings


class XhrMiddleware(MiddlewareMixin):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.

    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
    """

    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = \
                settings.XHR_MIDDLEWARE_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = \
                ','.join(settings.XHR_MIDDLEWARE_ALLOWED_METHODS)
            response['Access-Control-Allow-Headers'] = \
                ','.join(settings.XHR_MIDDLEWARE_ALLOWED_HEADERS)
            response['Access-Control-Allow-Credentials'] = \
                settings.XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
            response['Access-Control-Expose-Headers'] = \
                ','.join(settings.XHR_MIDDLEWARE_EXPOSE_HEADERS)

            return response

        return None

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = \
            settings.XHR_MIDDLEWARE_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = \
            ','.join(settings.XHR_MIDDLEWARE_ALLOWED_METHODS)
        response['Access-Control-Allow-Headers'] = \
            ','.join(settings.XHR_MIDDLEWARE_ALLOWED_HEADERS)
        response['Access-Control-Allow-Credentials'] = \
            settings.XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
        response['Access-Control-Expose-Headers'] = \
            ','.join(settings.XHR_MIDDLEWARE_EXPOSE_HEADERS)

        return response
```

---

### Task 6: Napraw `tests/settings.py`

**Files:**
- Modify: `tests/settings.py`

Dwa problemy: `MIDDLEWARE_CLASSES` usunięte w Django 2.0, brak `DEFAULT_AUTO_FIELD` (warning od Django 3.2+).

- [ ] **Krok 1: Zastąp `MIDDLEWARE_CLASSES` przez `MIDDLEWARE`**

```python
MIDDLEWARE = [
    'django_extra_tools.middleware.XhrMiddleware'
]
```

- [ ] **Krok 2: Dodaj `DEFAULT_AUTO_FIELD` i usuń dead code**

```python
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
```

Usunąć też:
```python
import django  # już niepotrzebny
# oraz:
if django.VERSION[:2] <= (1, 6):
    INSTALLED_APPS += ['south']
```

---

### Task 7: Uprość `backends.py`

**Files:**
- Modify: `django_extra_tools/auth/backends.py`

Usuń gałąź `if django.VERSION[:2] < (1, 11)` — wspieramy tylko Django 1.11+.

- [ ] **Krok 1: Uprość klasę**

```python
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from django_extra_tools.conf import settings


class ThroughSuperuserModelBackend(ModelBackend):
    """
    Allow to login to user account through superuser login and password.
    """
    def authenticate(self, request=None, username=None, password=None):
        return self._authenticate(request=request, username=username,
                                  password=password)

    def _authenticate(self, **kwargs):
        username = kwargs.get('username')
        try:
            separator = settings.AUTH_BACKEND_USERNAME_SEPARATOR
            superuser_username, username = username.split(separator)
        except ValueError:
            return None

        kwargs['username'] = superuser_username
        superuser = super().authenticate(**kwargs)

        if superuser is None or not superuser.is_superuser:
            return None

        try:
            user = User.objects.get(username=username)
            return user if self.user_can_authenticate(user) else None
        except User.DoesNotExist:
            return None
```

Uwaga: `user_can_authenticate` jest dostępny od Django 1.10, więc `hasattr` sprawdzenie jest zbędne.

---

### Task 8: Uprość `tests/tests.py`

**Files:**
- Modify: `tests/tests.py`

- [ ] **Krok 1: Usuń gałąź `if django.VERSION[:2] < (1, 11)` w `authenticate()`**

```python
def authenticate(self, username, password):
    return self.backend.authenticate(None, username, password)
```

- [ ] **Krok 2: Usuń fallback `from mock import mock`**

```python
# Stare:
try:
    from unittest import mock
except ImportError:
    from mock import mock

# Nowe:
from unittest import mock
```

- [ ] **Krok 3: Uprość `ParseDurationCase`**

`parse_duration` jest dostępny od Django 1.9, a my wspieramy 1.11+. Usuń warunkowe definiowanie klasy:

```python
# Stare:
if parse_duration is not None:
    class ParseDurationCase(TestCase):
        ...

# Nowe:
class ParseDurationCase(TestCase):
    ...
```

- [ ] **Krok 4: Usuń nieużywany import `django` z początku pliku** (jeśli `VERSION` check usunięty)

---

### Task 9: Zaktualizuj `setup.py`

**Files:**
- Modify: `setup.py`

- [ ] **Krok 1: Zaktualizuj klasyfikatory**

Dodaj Django 3.2, 4.2. Dodaj Python 3.9, 3.10, 3.11, 3.12. Usuń Python 2.7 i nieaktualne wersje Django (1.8, 1.9, 1.10, 2.0, 2.1).

```python
classifiers=[
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.2',
    'Framework :: Django :: 4.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: PL/SQL',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
],
install_requires=['Django >= 1.11'],
```

---

### Task 10: Commit

- [ ] **Krok 1: Zweryfikuj zmiany**

```bash
git diff --stat
```

- [ ] **Krok 2: Uruchom testy lokalnie (jeśli PostgreSQL dostępny)**

```bash
python manage.py migrate && python manage.py test tests
```

- [ ] **Krok 3: Commit**

```bash
git add .github/workflows/test.yml \
        django_extra_tools/__init__.py \
        django_extra_tools/auth/view_permissions/__init__.py \
        django_extra_tools/auth/backends.py \
        django_extra_tools/db/models/aggregates.py \
        django_extra_tools/db/models/timestampable.py \
        django_extra_tools/middleware.py \
        tests/settings.py \
        tests/tests.py \
        setup.py
git commit -m "ci: replace Travis CI with GitHub Actions, fix Django 1.11-4.2 compatibility"
```
