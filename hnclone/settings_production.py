import os
from .settings_base import *

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