'''
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
'''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_PATH, os.pardir))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aM2mSqJbYY32nkMiZEWTdxfZ21ewNZEoSyaRefHrMtAV6DqmYA'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped',
    'material',
    'material.admin',
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'bootstrap3',
    'easymoney',
    'phonenumber_field',
    'django_countries',
    'postal',
    'babel',
    'easy_thumbnails',
    'timezone_field',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'GroupInvitations',
    'BrownstoneTutors',
    'Student',
    'Tutor',
    'Client',
    'Subjects',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'NrFGkAnNdh',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

#ORGS_REGISTRATION_BACKEND = 'myapp.backends.MyRegistrationBackend'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'brownstonetestemail@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = '1234567890Josh'

EMAIL_USE_SSL = True

LOGIN_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'GroupInvitations.models.InvitationsAdapter'

INVITATIONS_ALLOWED_GROUPS = 'admin'
INVITATIONS_INVITATION_EXPIRY = 7
INVITATIONS_INVITATION_ONLY = True
INVITATIONS_SIGNUP_REDIRECT = 'account_signup'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'allauth.account.Profile'
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#AUTH_USER_MODEL = 'Profiles.Profile'

#ORGS_INVITATION_BACKEND = 'myapp.backends.MyInvitationBackend'

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = '/home/django/django_project/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

#STATICFILES_DIRS = (
#    #'django_google_maps/js/google-maps-admin.js',
#    os.path.join(PROJECT_DIR , 'static').replace('\\','/'),
#    os.path.join(PROJECT_DIR , '../static').replace('\\','/'),
#)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR , 'templates/').replace('\\','/'),
    os.path.join(PROJECT_DIR , '../templates/').replace('\\','/'),
    os.path.join(PROJECT_PATH, 'templates/'),
)

MEDIA_ROOT = '/home/django/django_project/media/'
MUGSHOT_PATH = 'mugshots/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'