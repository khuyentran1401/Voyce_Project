"""
Django settings for Project1 project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import yaml

with open("Project1/config.yaml") as file:

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    config = yaml.full_load(file)

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config['secret_key']

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # This setting is to specify your email service provider. We are using the setting for Gmail.
    EMAIL_HOST = config['email']['type']['gmail']
    EMAIL_USE_TLS = config['email']['use']['tls']
    EMAIL_USE_SSL = config['email']['use']['ssl']
    # This is the setting for Gmail, you can get yours on the web. It is the port used by the SMTP server.
    EMAIL_PORT = config['email']['port']
    EMAIL_HOST_USER = config['email']['host_user']
    EMAIL_HOST_PASSWORD = config['email']['host_password']
 
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # very important!!!
        'project_track.apps.ProjectTrackConfig',
        'table',
        'six'
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

    ROOT_URLCONF = 'Project1.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ["Project1/templates/"],
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

    WSGI_APPLICATION = 'Project1.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/['databases']['
    DATABASES = {
 
        'default': {
            'ENGINE': config['databases']['engine'],
            'NAME': config['databases']['name'],
            'USER': config['databases']['user'],
            'PASSWORD': config['databases']['password'],
            'HOST': config['databases']['host'],
            'PORT': config['databases']['port'],
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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATIC_URL = '/static/'

    '''
    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # This setting is to specify your email service provider. We are using the setting for Gmail.
    EMAIL_HOST = 'smtp.gmail.com'
    #EMAIL_HOST = 'smtp.outlook.com'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    # This is the setting for Gmail, you can get yours on the web. It is the port used by the SMTP server.
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'khuyentran1476@gmail.com'
    EMAIL_HOST_PASSWORD = 'Cun123456'
    # Application definition
    '''

