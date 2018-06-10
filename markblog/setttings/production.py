from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='    postgres://nwkuxgbswlkfga:531342bdd9dc6ce9a0aa46de736f5364641e2c650f334d1cce0b498f7289e96c@ec2-54-235-132-202.compute-1.amazonaws.com:5432/d6tkguqfbl5rgq'
)