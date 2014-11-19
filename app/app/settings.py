# app/settings.py
# Application settings required

from os.path import dirname, join


# Location of app directory
BASE_DIR    = dirname(dirname(__file__))
DOC_ROOT    = join(BASE_DIR,'user_doc')
LOG_DIR     = join(dirname(BASE_DIR), 'logs')
SCRIPTS_DIR = join(dirname(BASE_DIR), 'scripts')


# Error messages
DEBUG=True
TEMPLATE_DEBUG = True


# Routes
ROOT_URLCONF = 'app.urls'
    

# Login
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'


# Shim to run application from Apache
WSGI_APPLICATION = 'app.wsgi.application'
SECRET_KEY = 's!qs5!9(bhkv7#hn#172zm_*l#m)j(8lv1gj)#84p$9+^&amp;bn9e'


# Static server
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (  BASE_DIR+'/static', )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'doc',
    'note',
    'task',
    'util',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

 
# Loading templates
TEMPLATE_DIRS = (
    BASE_DIR+"/templates",
)

# Import external settings files
from db import DATABASES

# Amazon AWS SES Email Service
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_ACCESS_KEY_ID = 'AKIAJNEWSJNXFHEWAZ4A'
AWS_SES_SECRET_ACCESS_KEY = '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'
AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
AWS_SES_AUTO_THROTTLE = 0.5 # (default; safety factor applied to rate limit)
                            # Note: our current limit for SES is 5 emails per second
 
