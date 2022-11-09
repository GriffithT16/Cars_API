# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+z*=l&whjt%3+63tzf7pc2j)%cx*v!nxa_kc-fev413(^05lu*'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Bowhunt1'
    }
}