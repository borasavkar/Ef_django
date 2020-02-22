import os
from decouple import config
from google.oauth2 import service_account
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS = ['krediemekliye-django-server.azurewebsites.net']
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sayfalar.apps.SayfalarConfig',
    'users.apps.UsersConfig',
    'django_cleanup.apps.CleanupConfig',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ef_project.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ef_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'krediemekliyedb',
        'USER' : 'postgres',
        'PASSWORD' : 'GztBskTam35',
        'HOST' : 'localhost',
        'PORT' : '5432',

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/static/"),
    # '/var/www/static/',
]

SITE_ID = 1

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# LOGIN_REDIRECT_URL = "home"
LOGIN_REDIRECT_URL = "posts"
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER',default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD',default='')
# EMAIL_HOST_USER = 'borasavkar@gmail.com'
# EMAIL_HOST_PASSWORD = 'yfvb ifei lqor hxzk'
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID',default='')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY',default='')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME',default='')
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# AZURE_ACCOUNT_NAME = config('AZURE_ACCOUNT_NAME')
# AZURE_ACCOUNT_KEY = config('AZURE_ACCOUNT_KEY')
# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# key=API_KEY
# GOOGLE_APPLICATION_CREDENTIALS = os.path.join(BASE_DIR, 'krediemekliye-a9b836d8f5a9.json')
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     "E:\Django\KrediEmekkliye -Gcloud\Ef_project\krediemekliye-a9b836d8f5a9.json"
# )
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_BUCKET_NAME = 'krediemekliye'
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
