from .base import *
from .env import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ALLOWED_HOSTS = [env('ALLOWED_HOST')]
