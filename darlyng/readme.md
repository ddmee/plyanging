## Darlyng

Django based reading app for translations backed by Postgresql running on Docker.

## Docker

Start and stop the service with compose:

```shell
docker-compose --profile alpha up --build
# clear up
docker-compose down
```

Note, an appropriate `.env` file is required in the root of the project that initialises environment variables for the project. See `darlyng/enf_f.py` to workout what ought to go into the .env file. Anything without a 'default' value is probably required.

## Generating migrations

If the model changes, django will produce migration scripts for the changes. Need to run the manage.py inside the django container. Note, docker-compose should be setup to mount the migrations directory within each app to the host, so that the generated migration code can be saved by the host rather than languish in the container.

```shell
# Spin up the services with compose
docker-compose --profile alpha up --build
docker exec -it django /bin/bash
cd darlyng
pipenv shell
python manage.py makemigrations polls
python manage.py makemigrations reader
```

Note, you can run `python manage.py check` to check for any problems with the project without making migrations or running the database.

## Running migrations

Migrations can be run like so:

```shell
# run inside the container
pipenv run python darlyng/manage.py migrate
```

Note, `scripts/container_run.sh` runs the migrate command before starting the web-server. So you probably don't need to run migrate much.


## Django shell

Available with:

```shell
pipenv run python manage.py shell
```

## Admin panel

Admin panel ought to be available at `http://<host>/admin`

Creation of admin user:

```shell
pipenv run python manage.py createsuperuser
```

Note, `scripts/container_run.sh` should auto-run this with `--noinput` setting value of user from the .env file.
