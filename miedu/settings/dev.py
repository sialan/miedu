# python manage.py syncdb ->, python manage.py syncdb --settings=settings.development
from common import *
from os.path import join, normpath

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''
DIRECTORY = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT 
FILEBROWSER_MEDIA_URL = MEDIA_URL 
FILEBROWSER_STATIC_ROOT = STATIC_ROOT 
FILEBROWSER_STATIC_URL = STATIC_URL 

URL_FILEBROWSER_MEDIA = STATIC_URL + "filebrowser/"
PATH_FILEBROWSER_MEDIA = STATIC_ROOT + "filebrowser/"
URL_TINYMCE = STATIC_URL + "tiny_mce/"
PATH_TINYMCE = STATIC_ROOT + "tiny_mce/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'miedu/static',
)

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql', 'mysql', etc.
        'NAME': 'miedu_dev',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

MIDDLEWARE_CLASSES += (
	# 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (

)