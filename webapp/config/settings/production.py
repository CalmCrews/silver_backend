from .base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = False
ALLOWED_HOSTS = ['*']

# TODO: 프론트엔드 URL 배포 후 수정
FRONTEND_URL = "http://www.moyeo.store/"
BACKEND_URL = "http://101.101.209.172"

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
    "KAKAO_REDIRECT_URI": f"{FRONTEND_URL}/users/kakao/callback/",
}

NAVER_CONFIG = {
    "NAVER_CLIENT_ID": os.environ.get("NAVER_CLIENT_ID_PRODUCTION"),
    "NAVER_CLIENT_SECRET": os.environ.get("NAVER_CLIENT_SECRET_PRODUCTION"),
    "NAVER_REDIRECT_URI": f"{FRONTEND_URL}/users/naver/callback/",
}

CSRF_TRUSTED_ORIGINS = [
    BACKEND_URL,
]
