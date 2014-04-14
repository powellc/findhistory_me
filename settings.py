"""
Django settings for findhistory_me project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):

    ADMINS = (
        ('FindHistory Admin', 'info@findhistory.me'),
    )

    MANAGERS = ADMINS

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    USE_SOUTH = True

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "d1a1bdfd-d7ff-416c-b3d2-65bc5e3c4e04f65e3026-bf9b-43d7-ab43-e5623a9a7b5b1759e29e-25bf-47d0-a37b-f924755e45ba"

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = []

    PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"

    PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

    # Application definition

    INSTALLED_APPS = (
        "history_theme",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        "django.contrib.gis",
        "artifacts",
        "dajaxice",
        "sorl.thumbnail",
        "mezzanine.boot",
        "mezzanine.conf",
        "mezzanine.core",
        "mezzanine.generic",
        "mezzanine.blog",
        "mezzanine.forms",
        "mezzanine.pages",
        "mezzanine.galleries",
        "mezzanine.twitter",
        #"mezzanine.accounts",
        #"mezzanine.mobile",
        "django_extensions",
        "compressor",
        PACKAGE_NAME_FILEBROWSER,
        PACKAGE_NAME_GRAPPELLI,
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + \
        ("django.core.context_processors.request",
         "django.core.context_processors.tz",
         "mezzanine.conf.context_processors.settings",)

    MIDDLEWARE_CLASSES = (
        "mezzanine.core.middleware.UpdateCacheMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "mezzanine.core.request.CurrentRequestMiddleware",
        "mezzanine.core.middleware.RedirectFallbackMiddleware",
        "mezzanine.core.middleware.TemplateForDeviceMiddleware",
        "mezzanine.core.middleware.TemplateForHostMiddleware",
        "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
        "mezzanine.core.middleware.SitePermissionMiddleware",
        # Uncomment the following if using any of the SSL settings:
        # "mezzanine.core.middleware.SSLRedirectMiddleware",
        "mezzanine.pages.middleware.PageMiddleware",
        "mezzanine.core.middleware.FetchFromCacheMiddleware",
    )

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        'dajaxice.finders.DajaxiceFinder',
    )

    GOOGLE_API_KEY = "ABQIAAAATux_aKmAEX7DnojAr8SqlRRaty8kQfKELltUuVAn-OpfdO7k-xQ55ALwLa7MSyKCpJU1w0cHtjYMYw"

    AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    ROOT_URLCONF = 'urls'

    WSGI_APPLICATION = 'wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3'),
        environ=True))

    CACHES = values.CacheURLValue('memcached://127.0.0.1:11211')

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/New_York'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

    TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = 'findhistory_me'
    AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
                   'Cache-Control': 'max-age=86400', }

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 14

    LOGIN_EXEMPT_URLS = ['', '/',
                         '/accounts/login',
                         'login',
                         '/accounts/activate/']

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/home/'
    LOGOUT_URL = '/accounts/logout/'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
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


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = TEMPLATE_DEBUG = True

    DATABASES = values.DatabaseURLValue(
        'postgres://fhm:kjlkjzluijsdfkj@localhost/fhm')

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)

    DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = TEMPLATE_DEBUG = False

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue()

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    RAVEN_CONFIG = {
        'dsn': DSN_VALUE,
    }

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)
