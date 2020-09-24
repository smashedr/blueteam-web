#!/usr/bin/env sh

set -ex

python manage.py collectstatic --noinput

exec "$@"
