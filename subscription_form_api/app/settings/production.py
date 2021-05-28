from app.settings.common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# SSL/HTTPS
# https://docs.djangoproject.com/en/3.2/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True

SECURE_REDIRECT_EXEMPT = []

SESSION_COOKIE_SECURE = True


# CSRF
# Cross Site Request Forgery

CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv())


# HSTS
# https://docs.djangoproject.com/en/3.2/topics/security/

SECURE_HSTS_SECONDS = 5 * 60

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# Clickjacking
# https://docs.djangoproject.com/en/3.2/ref/clickjacking/

X_FRAME_OPTIONS = 'DENY'

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True


# Sessions
# https://docs.djangoproject.com/en/3.2/ref/settings/#sessions

SESSION_COOKIE_AGE = 24 * 60 * 60  # 24 hours, in seconds

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default=5432, cast=int),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')

STATIC_ROOT = config(
    'STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_DIRS = config(
    'STATICFILES_DIRS', default=os.path.join(BASE_DIR, 'static'), cast=Csv())


# Media files
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_URL = config('MEDIA_URL', default='/media/')

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))


# File upload
# https://docs.djangoproject.com/en/3.2/ref/settings/#file-upload-max-memory-size

FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5 MB

# https://docs.djangoproject.com/en/3.2/ref/settings/#file-upload-directory-permissions
FILE_UPLOAD_DIRECTORY_PERMISSIONS = config(
    'FILE_UPLOAD_DIRECTORY_PERMISSIONS', default=420, cast=int)  # 0o640 -rw-r-----

# https://docs.djangoproject.com/en/3.2/ref/settings/#file-upload-permissions
FILE_UPLOAD_PERMISSIONS = config(
    'FILE_UPLOAD_PERMISSIONS', default=420, cast=int)  # 0o640 -rw-r-----

# https://docs.djangoproject.com/en/3.2/ref/settings/#file-upload-temp-dir
FILE_UPLOAD_TEMP_DIR = config(
    'FILE_UPLOAD_TEMP_DIR', default=384, cast=int)  # 0o600 drw-------

# Data upload
# https://docs.djangoproject.com/en/3.2/ref/settings/#data-upload-max-memory-size

DATA_UPLOAD_MAX_MEMORY_SIZE = 102400  # 100 KB

# https://docs.djangoproject.com/en/3.2/ref/settings/#data-upload-max-number-fields
DATA_UPLOAD_MAX_NUMBER_FIELDS = 64
