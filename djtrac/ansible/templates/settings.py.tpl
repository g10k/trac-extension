import os

from djtrac.settings_default import *

DEBUG = True
SECRET_KEY = '123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djtrac/extra.db'),
    },
    'trac_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djtrac/trac.db'),
    },

}