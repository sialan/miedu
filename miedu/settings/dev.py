from common import *
from os.path import join, normpath


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# URL prefix for static files./
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images. Make sure to use a trailing slash.
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

FILEBROWSER_MEDIA_ROOT = normpath(MEDIA_ROOT)
FILEBROWSER_MEDIA_URL = normpath(MEDIA_URL)
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_STATIC_ROOT = normpath(STATIC_ROOT)
FILEBROWSER_STATIC_URL = normpath(STATIC_URL)

FILEBROWSER_URL_FILEBROWSER_MEDIA = join(STATIC_URL, "filebrowser/")
FILEBROWSER_PATH_FILEBROWSER_MEDIA = join(STATIC_ROOT, "filebrowser")
FILEBROWSER_URL_TINYMCE = normpath(join(STATIC_URL, "tiny_mce/jscripts/tiny_mce/"))
FILEBROWSER_PATH_TINYMCE = normpath(join(STATIC_ROOT, "tiny_mce/jscripts/tiny_mce/"))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'miedu/static',
)

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql', 'mysql', etc.
        'NAME': join(SITE_ROOT, 'miedu_dev_v1',                      # Or path to database file if using sqlite3.
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