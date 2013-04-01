import sys
from os.path import basename, dirname, join, normpath, realpath

ADMINS = (
    ('Alan Si', 'si.alan090@gmail.com'),
)

MANAGERS = ADMINS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(realpath(__file__)))

# Absolute filesystem path to the top-level project folder.
PROJECT_ROOT = dirname(DJANGO_ROOT)

# Absolute filesystem path to the whole site folder.
SITE_ROOT = dirname(PROJECT_ROOT)

# Site name
SITE_NAME = basename(DJANGO_ROOT)

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT)
sys.path.append(DJANGO_ROOT)
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
sys.path.append(normpath(join(DJANGO_ROOT, 'main')))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gidvq5!54rs7r8y*s)9d=w+jd$(qd5^s*#^$qdsqzcxbo1-ymf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'miedu.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'miedu.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'miedu/templates',
    'miedu/main/home/templates',
    'miedu/main/accounts/templates',
    'miedu/main/articles/templates',
    'miedu/main/campaigns/templates',
    'miedu/main/plans/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'taggit',
    'accounts',
    'articles',
    'blogs',
    'campaigns',
    'exercises',
    'lessons',
    'multimedia',
    'plans',
    'projects',
    'tags',
    'transactions',
    'south',
    'storages',
    'social_auth',
    'billing',

)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
)

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''

AUTH_USER_MODEL = 'accounts.Account'
GRAPPELLI_ADMIN_TITLE = 'locallaunch'

MERCHANT_TEST_MODE = True # Toggle for live
MERCHANT_SETTINGS = {
    "stripe": {
        "API_KEY": "",
        "PUBLISHABLE_KEY": "", # Used for stripe integration
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
