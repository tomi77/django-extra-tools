#!/usr/bin/env bash

CNT=`python manage.py|grep syncdb|wc -l`

if [ $CNT -gt 0 ]; then
    python manage.py syncdb --noinput
fi