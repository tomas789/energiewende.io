import os
from .settings_base import *


ALLOWED_HOSTS = [
    'energiewende.io',
    'www.energiewende.io',
    'ipv6.energiewende.io'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['ENERGIEWENDE_DB_NAME'],
        'USER': os.environ['ENERGIEWENDE_DB_USER'],
        'PASSWORD': os.environ['ENERGIEWENDE_DB_PASSWORD'],
        'HOST': os.environ['ENERGIEWENDE_DB_HOST'],
        'PORT': '',
    }
}