from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Connect to Neo4j Database
config.DATABASE_URL = 'bolt://paradisepapers:paradisepapers@174.138.63.95:7687'  # default


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ALLOWED_HOSTS = []
