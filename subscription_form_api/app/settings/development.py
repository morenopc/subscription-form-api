from app.settings.common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = Path(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    Path(BASE_DIR, 'static'),
    Path(BASE_DIR, 'settings'),
]


# Media files
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_URL = '/media/'

MEDIA_ROOT = Path(BASE_DIR, 'media')
