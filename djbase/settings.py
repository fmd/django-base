"""
Django settings for djbase project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import lazyconf
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

lazy = lazyconf.Lazyconf().load(BASE_DIR)

SECRET_KEY = lazy.get('env.secret_key')

DEBUG = lazy.get('env.debug')
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our apps
    'djbase.apps.frontend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djbase.urls'

WSGI_APPLICATION = 'djbase.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

if lazy.get('db._enabled'):
    DATABASES = {
        'default': {
            'ENGINE': lazy.get('db.engine'),
            'NAME': lazy.get('db.name'),
        }
    }

if lazy.get('db.user'):
    DATABASES['default']['USER'] = lazy.get('db.user')

if lazy.get('db.pass'):
    DATABASES['default']['PASS'] = lazy.get('db.pass')

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
