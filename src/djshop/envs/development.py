from .common import *


ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   'daphne',
   'drf_spectacular',
] + INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djshop',
        'USER': 'djshop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}
