from .common import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Cookies setup http or https
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# You are using postgresSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# def your app domain , dont leave '*' in production
ALLOWED_HOSTS = ['*']



