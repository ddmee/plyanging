"""Application configuration from env file
"""
# stdlib
from secrets import choice
# third party
from environs import Env

env = Env(expand_vars=True)
env.read_env()

# http://sentry.io where to sent events
SENTRY_DSN = env.str("SENTRY_DSN", default=None)

POSTGRES_HOST = env.str("POSTGRES_HOST", default='database')
POSTGRES_PORT = env.str("POSTGRES_PORT", default='5432')
POSTGRES_USER = env.str("POSTGRES_USER", default='postgres')
POSTGRES_DB = env.str("POSTGRES_DB", default='postgres')
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")

# Using `manage.py createsuperuser --noinput` ought to take these values
# from environment variables. See https://stackoverflow.com/a/59467533/4498470
# Should allow scripting creation of admin super-user.
DJANGO_SUPERUSER_USERNAME = env.str("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_EMAIL = env.str("DJANGO_SUPERUSER_EMAIL")
DJANGO_SUPERUSER_PASSWORD = env.str("DJANGO_SUPERUSER_PASSWORD")


chars = (r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"'
         r'#$%&()*+-:;^_`{|}~')

DJANGO_SECRET_KEY = env.str("DJANGO_SECRET_KEY",
                            default=''.join(choice(chars) for x in range(50)))
