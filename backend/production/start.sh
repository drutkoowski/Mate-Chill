#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python manage.py migrate
exec gunicorn mate.wsgi --bind 0.0.0.0:8000