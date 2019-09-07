"""
Django settings for zrcms project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from env_vars import ENVIRONMENT
from zrcms.env_vars import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'zrcommission',
    'zrcomms',
    'zrmapping',
    'zrpayment',
    'zrtransaction',
    'zruser',
    'zrutils',
    'zrwallet',
    'debug_toolbar',
    'loan',
    'feedback'
]

EXTERNAL_APPS = [
    'rest_framework',
    'corsheaders',
    'widget_tweaks',
]

INSTALLED_APPS = INTERNAL_APPS + PROJECT_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'zrcms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'zrcms.wsgi.application'


# For CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = []

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if ENVIRONMENT == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dfsgpmoh5tgdjp',
            'USER': 'mmbunvblidzaqk',
            'PASSWORD': 'e11a7554a633d40c59256c91db24712310769e494652d3fce09862305ca4d754',
            'HOST': 'ec2-54-75-239-237.eu-west-1.compute.amazonaws.com',
            'PORT': '5432'

        }
    }
else:
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config()
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'  # static folders location in each of the app

STATICFILES_DIRS = (
    # will not be server from here, long term storage only
    os.path.join(BASE_DIR, 'static-storage'),
)

# will get server from here, static-serve
STATIC_ROOT = os.path.join(BASE_DIR, 'static-serve')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
S3_AWS_SEC_KEY_ID = 'AKIAI4Y5NO3K36LXYYVQ'
S3_AWS_SEC_KEY_SECRET = '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'


# BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
FROM_EMAIL = 'noreply@zrupee.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@zrupee.com'
EMAIL_HOST_PASSWORD = 'Anwesha@2020'
EMAIL_USE_SSL = True
EMAIL_PORT = 465

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'zrcms.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

INSTALLED_APPS += ("djcelery", )

SETUP = os.environ.get('SETUP', '')
if SETUP == 'heroku':
    BROKER_HOST = 'impala.rmq.cloudamqp.com'
    BROKER_PORT = 5672
    BROKER_USER = 'cwolziqk'
    BROKER_PASSWORD = '_DmFPc9QiXp_gF8AfrBBu_PlDmkyxtzn'
    BROKER_VHOST = 'cwolziqk'

    UPI_URL = 'http://114.143.22.139/'
    UPI_API_PASSWORD = "EE560B75E235E2180107D0160"
    UPI_PAY_PRO_MID = "1263"
    UPI_SECRET = "D22qbAyeMaY1MW6FX2+23Q=="
    UPI_PARTNER_ID = "P1263"
elif SETUP == 'prod':
    BROKER_HOST = "172.17.0.1"
    BROKER_BACKEND="redis"
    REDIS_PORT = 6379
    REDIS_HOST = "172.17.0.1"
    BROKER_USER = ""
    BROKER_PASSWORD = ""
    BROKER_VHOST = "0"
    REDIS_DB = 0
    REDIS_CONNECT_RETRY = True
    CELERY_SEND_EVENTS = True

    UPI_URL = 'https://mosambee.cash/PayProWebService/live/upi/statusCall/'
    UPI_API_PASSWORD = "73A2AEC172534D23975D05093"
    UPI_PAY_PRO_MID = "89218"
    UPI_SECRET = "LZpydM6fLcMULdgnd6dxOA=="
    UPI_PARTNER_ID = "M89218"
else:
    BROKER_URL = 'redis://localhost:6379/'
    #BROKER_HOST = 'localhost'
    #BROKER_PORT = 6379

    UPI_URL = 'http://114.143.22.139/'
    UPI_API_PASSWORD = "EE560B75E235E2180107D0160"
    UPI_PAY_PRO_MID = "1263"
    UPI_SECRET = "D22qbAyeMaY1MW6FX2+23Q=="
    UPI_PARTNER_ID = "P1263"

import djcelery
djcelery.setup_loader()

REPORTS_PATH = os.path.join(BASE_DIR, 'media', 'report')
if not os.path.exists(REPORTS_PATH):
    os.makedirs(REPORTS_PATH)


try:
    from local_settings import *
except ImportError:
    pass

TO_BANK = {'UTIB': '918020030276406', 'ICIC': '001105026711', 'INDB': '201001458436', 'SBIN': '32910001AADCL2120N'}

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

HAPPYLOAN_DISBURSE_ACC = {
    'ACCOUNT_NAME': 'Lalwani Innovations Private Limited',
    'CODE': 'UTIB',
    'ACCOUNT_NO': '918020030276406',
    'IFSC': 'UTIB0000373'
}

HAPPYLOAN_REPAYMENT_ACC = {
    'ACCOUNT_NAME': 'Arthimpact Finserve Private Limited',
    'CODE': 'RBLL',
    'ACCOUNT_NO': '409000578256',
    'IFSC': 'RATN0000088'
}
