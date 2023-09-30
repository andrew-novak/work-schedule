"""
Django settings for config project.

Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import sys
import environ

env = environ.Env()
default_runserver_port = "3000"
is_dev = "runserver" in sys.argv

env_vars = {
    "HOST": env.str("WORK_SCHEDULE_HOST"),
    "DJANGO_SECRET_KEY": env.str("WORK_SCHEDULE_DJANGO_SECRET_KEY"),
    "DB_NAME": env.str("WORK_SCHEDULE_DB_NAME"),
    "DB_USER": env.str("WORK_SCHEDULE_DB_USER"),
    "DB_PASSWORD": env.str("WORK_SCHEDULE_DB_PASSWORD"),
    "STATIC_ROOT": env.str("WORK_SCHEDULE_STATIC_ROOT"),
    # Optional, use a path without a trailing slash, e.g. "/apps/app1"
    "SUBLOCATION": env.str("WORK_SCHEDULE_SUBLOCATION")
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if "SUBLOCATION" in env_vars:
    FORCE_SCRIPT_NAME = env_vars.get("SUBLOCATION")

SECRET_KEY = env_vars.get("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    env_vars.get("HOST")
]

CSRF_TRUSTED_ORIGINS = [
    "https://*." + env_vars.get("HOST")
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'schedule',
    #'bootstrap5' <-- for django-bootstrap-v5
    'django_bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env_vars.get("DB_NAME"),
        "USER": env_vars.get("DB_USER"),
        "PASSWORD": env_vars.get("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
    #   'NAME': 'config.password_validation.Validator'
    #}
    #Default:
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GB'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = env_vars.get("STATIC_ROOT")

STATIC_URL = 'static/'
if "SUBLOCATION" in env_vars:
    STATIC_URL = env_vars.get("SUBLOCATION") + '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
if "SUBLOCATION" in env_vars:
    LOGIN_REDIRECT_URL =  env_vars.get("SUBLOCATION") + "/"
    LOGOUT_REDIRECT_URL = env_vars.get("SUBLOCATION") + "/"
