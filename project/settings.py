import os
from environs import Env
import dj_database_url

env = Env()
env.read_env()
with env.prefixed("DB_"):
    DATABASES = {
        'default': dj_database_url.config(default=f"{env('ENGINE')}://{env('USER')}:{env('PASSWORD')}"
                                                  f"@{env('HOST')}:{env('PORT')}/{env('NAME')}")
    }

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
