from common import *
from os.path import join, normpath

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

DEFAULT_FILE_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
AWS_STORAGE_BUCKET_NAME = aws_storage_bucketname

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

AWS_ACCESS_KEY_ID = aws_access_key_id 
AWS_SECRET_ACCESS_KEY = aws_secret_access_key

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# URL prefix for static files./
# Example: "http)://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
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
    ("css", normpath(join(DJANGO_ROOT, 'static/css'))),
    ("img", normpath(join(DJANGO_ROOT, 'static/img'))),
    ("js", normpath(join(DJANGO_ROOT, 'static/js'))),
)

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql', 'mysql', etc.
        'NAME': staging_database_name,                      # Or path to database file if using sqlite3.
        'USER': staging_database_user,
        'PASSWORD': staging_database_password,
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
            "read_default_file": normpath(join(PROJECT_ROOT, 'etcs/my.cnf')),
        }
    }
}

MIDDLEWARE_CLASSES += (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'gunicorn',
)
