from generated_config import *

DEBUG = FAB_DEBUG
DATABASES = {
    'default': {
        'ENGINE': FAB_DB_ENGINE,
        'NAME': FAB_DB_NAME,
        'USER': FAB_DB_USER,
        'PASSWORD': FAB_DB_PASS,
        'HOST': '',
        'PORT': '',
    }
}