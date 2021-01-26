from .base import *
from .env import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#Connect to Neo4j Database
config.DATABASE_URL = env('DATABASE_URL')  # default


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ALLOWED_HOSTS = [env('ALLOWED_HOST')]
