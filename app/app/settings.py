# app/settings.py
# Application settings required

from os.path import dirname, join

# Error messages
DEBUG=True
TEMPLATE_DEBUG = True


# Location of app directory
BASE_DIR = dirname(dirname(__file__))
DOC_ROOT = join(BASE_DIR,'user_doc')
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
#    'brain'
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


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'data', 'brain.db'),
    }
}


