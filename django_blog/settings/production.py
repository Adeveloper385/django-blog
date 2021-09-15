from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['djangoblogtemplate.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycogp2',
        'NAME': 'dbffhn4tvch48q',
        'PORT': 5432,
        'USER': 'ltyxzztyhxxsqo',
        'PASSWORD': 'af09e2e34e581fc962eac7adb4607124653a2d9d13e4f46e201f0636c7bc84bc',
        'HOST': 'ec2-44-198-146-224.compute-1.amazonaws.com'
    }
}

