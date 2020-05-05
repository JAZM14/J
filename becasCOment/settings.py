"""
Django settings for becas project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os #Nos permite acceder a funcionalidades dependientes del sistema operativa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #La base de datos esta unida al sistema del programa para dar funcionalidades
PATH_MEDIA = BASE_DIR+'/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ljfsc_fnc22@6j8*pc+)_l1g8nnv$ch!8h8c^fpvg45t56jzh' #Es una contraseña segura y oculta para evitar que la usen sin tu consentimiento

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] #Donde se aloja el host


# Application definition

INSTALLED_APPS = [#Las aplicaciones que requerimos
    'django.contrib.admin',#Nuestro superUsuario
    'django.contrib.auth',#para la seguridad
    'django.contrib.contenttypes',#Sirve para representar y almacenar informacion sobre los modelos instalados
    'django.contrib.sessions',#Para el uso de sesiónes de usuarios
    'django.contrib.messages',#para seccion de mensajes
    'django.contrib.staticfiles',#Usado para almavenar y manipular archivos estaticos
    'bases', #para el uso de bases
    'import_export', #nuestro sistema para poder mantener conectados nuestros archivos
    'solicitudes',
]

MIDDLEWARE = #Para la protección de la paguina y programa
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'becas.urls' #la configuración de las urls becas

TEMPLATES = [ #La confi de la visualización en la pagina
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'becas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = { #BAse de datos
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ #Para la validación de contraseñas
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-MX' #Para la confi del lenguaje en el que estara la pagina

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
