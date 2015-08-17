# -*- encoding: utf-8 -*-
"""
Django settings for djtrac project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #
    'djtrac',
    'django_select2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'djtrac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
            ],
        },
    },
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.messages.context_processors.messages',
#     'django.core.context_processors.request',
#     'django.core.context_processors.debug',
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.static',
#     'django.core.context_processors.media',
# )


WSGI_APPLICATION = 'djtrac.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'djtrac',
        'USER': 'djtrac',
        'PASSWORD': 'djtrac_pass',
        'HOST': '127.0.0.1',
        # 'PORT': '5432',

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

DATABASE_ROUTERS = ['djtrac.db_router.AuthRouter',]




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/'
#
# LOGIN_REQUIRED_URLS = (
#     r'/(.*)$',
# )
# LOGIN_REQUIRED_URLS_EXCEPTIONS = (
#     r'/admin/(.*)$',
#     r'/login(.*)$',
# )



LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.cproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


HTTP_PATH_TO_TRAC = 'https://trac.soft-way.biz/neo/ticket/'