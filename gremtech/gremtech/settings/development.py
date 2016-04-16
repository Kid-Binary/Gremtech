from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'Something secret steers at us!'

INSTALLED_APPS += [
    'debug_toolbar',
]

# Email

EMAIL_HOST = '62.205.128.183'
EMAIL_HOST_USER = 'info@gremtech.com.ua'
EMAIL_HOST_PASSWORD = '@#MeG@P$sw0rd42'

EMAIL_FROM = 'info@gremtech.com.ua'
EMAIL_TO = 'info@gremtech.com.ua'
