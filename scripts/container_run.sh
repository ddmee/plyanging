#!/bin/bash
pipenv run python darlyng/manage.py migrate
pipenv run python darlyng/manage.py createsuperuser --noinput
pipenv run python darlyng/manage.py generateschema --file darlyng/reader/static/reader/openapi-schema.yml
pipenv run python darlyng/manage.py runserver 0.0.0.0:80
