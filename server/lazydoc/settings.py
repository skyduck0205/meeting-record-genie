# -*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'notasecret'

ROOT_URLCONF = 'lazydoc.urls'

#
# Path and directories
#
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PDF_PATH = os.path.join(BASE_DIR, 'pdfs')
RST_PATH = os.path.join(BASE_DIR, 'rsts')
RST_BUILD_PATH = os.path.join(BASE_DIR, 'rst_build')

TEMPLATE_PATH = os.path.join(BASE_DIR, 'lazydoc/templates')
TEMPLATE_IMG_PATH = os.path.join(BASE_DIR, 'lazydoc/templates/img')

DATABASES = {}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_extensions',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

#
# Area settings
#
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = False
