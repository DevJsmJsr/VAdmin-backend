#!/bin/sh

alias poetry=/root/.local/bin/poetry

# apply database migrations
echo "---apply database migrations---"
poetry run python manage.py migrate

# runserver
echo "---run server---"
poetry run python manage.py runserver 0.0.0.0:8000