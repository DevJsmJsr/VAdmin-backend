import os
import psycopg2.extensions

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DB_DATABASE'],
    'USER': os.environ['DB_USERNAME'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
    'OPTIONS': {
      'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
  }
}


DEBUG = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REDIRECT_EXEMPT = []
SECURE_PROXY_SLL_HEADER = ('HTTP_X_FORWARDED_PHOTO', 'https')
