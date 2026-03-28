# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`django-extra-tools` is a Django utility library providing database aggregates, model mixins, template filters, middleware, authentication backends, and management command base classes. Requires PostgreSQL.

## Commands

### Running Tests

```bash
# Full test suite
python manage.py test tests

# Single test case
python manage.py test tests.tests.FirstTestCase

# With coverage
coverage run manage.py test tests
coverage report
```

### Setup for Development

```bash
pip install psycopg2-binary pyyaml
# Requires a PostgreSQL database configured in tests/settings.py
python manage.py migrate
```

## Architecture

### Package Structure

- `django_extra_tools/db/models/` — Database utilities
  - `aggregates.py` — PostgreSQL-specific SQL aggregates: `First`, `Last`, `Median`, `StringAgg`
  - `timestampable.py` — Model mixins: `CreatedAtMixin`, `UpdatedAtMixin`, `DeletedAtMixin` and their `*ByMixin` variants that track the acting user
- `django_extra_tools/auth/` — Authentication
  - `backends.py` — `ThroughSuperuserModelBackend`: allows superusers to log in as other users via `superuser:username` format
  - `view_permissions/` — Django app that auto-generates `view_*` permissions via migrations
- `django_extra_tools/middleware.py` — `XhrMiddleware` for cross-domain XHR via postMessage
- `django_extra_tools/management.py` — Base classes: `OneInstanceCommand` (single-instance locking), `NagiosCheckCommand` (monitoring checks)
- `django_extra_tools/lockers.py` — Script locking: `FileLocker` (default) and `CacheLocker`
- `django_extra_tools/templatetags/parse.py` — Template filters: `parse_datetime`, `parse_date`, `parse_time`, `parse_duration`
- `django_extra_tools/http.py` — `HttpResponseGetFile` for file download responses
- `django_extra_tools/wsgi_request.py` — `get_client_ip(request)` with proxy support
- `django_extra_tools/conf/defaults.py` — All configurable settings with defaults

### Key Design Patterns

**Model mixins** use `save_by(user)` / `delete_by(user)` methods (not overriding `save()`/`delete()`) for user tracking to avoid signature conflicts.

**SQL aggregates** (`First`, `Last`, `Median`) rely on custom PostgreSQL SQL functions stored in `django_extra_tools/sql/`. These are loaded via migrations.

**Management command base classes** require subclasses to implement `handle_instance()` (for `OneInstanceCommand`) rather than `handle()`.

**Locking** is configurable globally via `DEFAULT_LOCKER_CLASS` setting; individual commands can also specify their locker.

### Test Configuration

Tests live in `tests/` with their own Django settings at `tests/settings.py`. The test project uses PostgreSQL and loads YAML fixtures from `tests/fixtures/`.

### Settings Reference

All defaults are in `django_extra_tools/conf/defaults.py`:
- `AUTH_BACKEND_USERNAME_SEPARATOR` — separator for through-superuser login (default: `:`)
- `XHR_MIDDLEWARE_ALLOWED_ORIGINS/METHODS/HEADERS/CREDENTIALS/EXPOSE_HEADERS` — CORS-like XHR middleware config
- `PRIVATE_IPS_PREFIX` — prefixes treated as private IPs by `get_client_ip`
- `DEFAULT_LOCKER_CLASS` — locking backend for `OneInstanceCommand`
