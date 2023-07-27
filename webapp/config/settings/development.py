from .base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True
ALLOWED_HOSTS = ['*']

BACKEND_URL = "http://localhost:8888"

DATABASES = (
    {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("POSTGRES_DB"),
            'USER': os.environ.get("POSTGRES_USER"),
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
            'HOST': 'db',
            'PORT': os.environ.get("POSTGRES_PORT"),
        }
    }
)

KAKAO_CONFIG = {
    "KAKAO_REST_API_KEY": os.environ.get("KAKAO_REST_API_KEY"),
    "KAKAO_REDIRECT_URI": f"{BACKEND_URL}/users/kakao/callback/",
}
