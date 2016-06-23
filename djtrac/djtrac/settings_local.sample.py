import os


SECRET_KEY = '123'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djtrac/extra.db'),
         'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'djtrac/test_extra.db'),
        }

    },
    'trac_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djtrac/trac.db'),
         'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'djtrac/test_trac.db'),
        }
    },

}

EMAIL_HOST_USER = 'support@compain.biz'
EMAIL_HOST_PASSWORD = '123'

PROJECT_URL = 'http://project.com'
