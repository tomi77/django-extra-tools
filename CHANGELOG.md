## master

* Added `ThroughSuperuserModelBackend`
* Make list of local IP's for ``get_client_ip`` configurable
* Added `lock` function that uses `FileLocker` or `CacheLocker` to lock multiple script executions
* Added post migrate hook to create `view_*` permissions for all content types

## 0.3.0

* Added `NagiosCheckCommand` management command
* Added support for Django >= 1.10 for Aggregate functions
* Added `timestampable` model mixins

## 0.2.0b1

* Added `XhrMiddleware`
* Fix for older Django (older Django does not have `django.utils.dateparse.parse_duration`)

## 0.1.0b2

* Initial release
