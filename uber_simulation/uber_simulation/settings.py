"""
Django settings for uber_simulation project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-abgl37@fmnn75m*qxsa&r-=&f7=f-)b1j47z#^u($%0udpzi22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'driver',
    'rest_framework.authtoken',
    'users',
    'billing',
    'rides',
    'administrator',
    'django_redis',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'django_extensions',
    'drf_yasg',
    'channels',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
AUTH_USER_MODEL = 'administrator.Administrator'

AUTHENTICATION_BACKENDS = [
    'administrator.authentication.AdministratorBackend',
    'django.contrib.auth.backends.ModelBackend',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = ['*']
# CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization', 'X-CSRFToken', 'Access-Control-Allow-Origin', 'authorization']
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]

# Allow all methods
# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]
ROOT_URLCONF = 'uber_simulation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'uber_simulation.wsgi.application'
# WSGI_APPLICATION = 'ubereats.wsgi.application'
ASGI_APPLICATION = 'uber_simulation.asgi.application'

# Redis configuration for Channel layers
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(os.getenv("REDIS_HOST"), 6379)],  # Ensure Redis is running on this host/port
        },
    },
}

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE'), #take from env
        'USER': os.getenv('MYSQL_USER'), # Replace with your MySQL username from enev
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'), # Replace with your MySQL server host form env
        'PORT': '3306',
        'OPTIONS': {
            'auth_plugin': 'mysql_native_password',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'"
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'driver.Driver'
#AUTH_USER_MODEL = 'administrator.Administrator'

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
SESSION_COOKIE_AGE = 60 * 60 * 24 * 5  # 5 days
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#Google Maps API Key
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
#Caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:6379/1".format(os.getenv("REDIS_HOST")),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

# # Kafka Configuration
# KAFKA_BROKER = 'localhost:9092'
# BILLING_EVENTS_TOPIC = 'billing-events'

KAFKA_BOKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","uber")

# print(KAFKA_BOKER, KAFKA_TOPIC)
print(KAFKA_BOKER, KAFKA_TOPIC)
