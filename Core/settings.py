"""
Django settings for Core project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import dj_database_url
from pathlib import Path
import os
# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-jl024#)=snl-7aynr#r=dwqz1ji3u*-qo3&r4u2l#maj!z8_58'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=True, cast=bool)
DEBUG=False
ALLOWED_HOSTS = ['smart-city-traffic-management-system.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Users",
    "Traffic_Spots",
    "Traffic_Analysis_and_Reommendations",
    "location_field.apps.DefaultConfig",
    "geopy",
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


CSRF_COOKIE_SECURE = False

CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Dashboard.context_processors.all_apps_context',  # Add your custom context processor

            ],
        },
    },
]

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse('postgresql://trafficmonitoringdb_wnna_user:2LhB7K0DB2gj1KKEPCzifRVpRqN16R9F@dpg-ct9n42qlqhvc73ekjuag-a.oregon-postgres.render.com/trafficmonitoringdb_wnna')

# Redirect URLs after login/logout
LOGIN_REDIRECT_URL = 'Dashboard:index'
LOGOUT_REDIRECT_URL = 'users:login'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    "Core/static",
]

# media files configuratino start

# The URL that will serve media files
MEDIA_URL = '/media/'

# The directory where uploaded media files will be stored on the server
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# media files configuratino end
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# APIs configuration 

# GOOGLE_API_KEY = config('GOOGLE_API_KEY')
GOOGLE_API_KEY = 'AIzaSyCMStVxIAgJETgmkls2wGVe_VU-YCscJIU'

OPENAI_API_KEY =''

LOCATION_FIELD = {
    "search.provider": "google",
    "provider.google.api": "//maps.google.com/maps/api/js?sensor=false",
    "provider.google.api_key": GOOGLE_API_KEY,
    "provider.google.api_libraries": "places",
    "provider.google.map.type": "ROADMAP",
}