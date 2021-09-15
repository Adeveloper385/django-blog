from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['template-for-django-blog.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddl9k07mlf85gh',
        'PORT': 5432,
        'USER': 'sgejenqmzqaqrk',
        'PASSWORD': '7659dfb7917e2246f729f0da9efd90c810a26f8fc555acec670c7cb7e5344bd2',
        'HOST': 'ec2-34-228-154-153.compute-1.amazonaws.com'
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
STATIC_ROOT = 'template-for-django-blog/heroku.com/static'
