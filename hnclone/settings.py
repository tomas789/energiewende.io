import os
from .settings_base import *


ALLOWED_HOSTS = [
    'localhost',
]


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}