import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = keep the secret key used in production secret!
SECRET_KEY = 'Q9bw#3$567$@qsdf'

# SECRET_KEY = keep the secret key used in production secret!
DEBUG = False # This was set to false to activate production mode

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth', 
   'django.contrib.contenttypes',
   'django.contrib.session',
   'django.contrib.messages',
   'django.contrib.staticfiles'
   'delivery', # My Delivery App
   'users', # Users App
]
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.messages.middleware.AuthenticationMiddleware'
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
   {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [BASE_DIR/' ']
      'APP_DIRS': True,
      'OPTION': {
         'context_processors': [
            'django.template.context_processors.debug',
             'django.template.context_processors.request',
             'django.contrib.auth.context_processors.auth',
             'django.contrib.messages.context_processors.messages',
         ],
         },
         },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
 'default': {
    'ENGINE': 'django.db.backends.postgresql'
    'NAME': ' '
    'USER': ' '
    'PASSWORD': ' '
    'HOST': 'local host'
    'PORT': 
 }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
