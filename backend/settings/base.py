import os
import sys
from datetime import timedelta

from django.core.exceptions import ImproperlyConfigured

from configurations import Configuration, values


class Base(Configuration):
    """
    Базовые настройки приложения
    """
    # Базовая директория приложения
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Список разрешённых хостов, переменная окружения DJANGO_ALLOWED_HOSTS
    ALLOWED_HOSTS = values.ListValue(['*'])

    # Секретный ключ приложения, переменная окружения DJANGO_SECRET_KEY
    SECRET_KEY = values.SecretValue()

    # Коннект к БД, переменная окружения DATABASE_URL=postgres://myuser@localhost/db
    DATABASES = values.DatabaseURLValue(conn_max_age=60)

    # Бэкенд аутенфикации Django
    AUTHENTICATION_BACKEND = values.ListValue([''])

    ROOT_URLCONF = values.Value('backend.urls')

    AUTH_USER_MODEL = values.Value('core.TMAbstractUser')

    WSGI_APPLICATION = values.Value('backend.wsgi.application')

    REST_FRAMEWORK = values.DictValue({
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'core.auth.CsrfExemptSessionAuthentication',
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'UNAUTHENTICATED_USER': None,
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_PAGINATION_CLASS': 'backend.apps.api.paginations.common.StandardResultsSetPagination'
    })

    # Настройки SMTP сервера
    EMAIL_USE_TLS = values.BooleanValue(True)
    EMAIL_HOST = values.Value('smtp.gmail.com')
    EMAIL_HOST_USER = values.Value('')
    EMAIL_HOST_PASSWORD = values.Value('')
    EMAIL_PORT = 587

    # Настройки JSON токенов
    JWT_AUTH = values.DictValue({
        'JWT_ENCODE_HANDLER':
            'rest_framework_jwt.utils.jwt_encode_handler',

        'JWT_DECODE_HANDLER':
            'rest_framework_jwt.utils.jwt_decode_handler',

        'JWT_PAYLOAD_HANDLER':
            'rest_framework_jwt.utils.jwt_payload_handler',

        'JWT_PAYLOAD_GET_USER_ID_HANDLER':
            'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

        'JWT_RESPONSE_PAYLOAD_HANDLER':
            'rest_framework_jwt.utils.jwt_response_payload_handler',

        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_GET_USER_SECRET_KEY': None,
        'JWT_PUBLIC_KEY': None,
        'JWT_PRIVATE_KEY': None,
        'JWT_ALGORITHM': 'HS256',
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_LEEWAY': 0,
        'JWT_EXPIRATION_DELTA': timedelta(seconds=300),
        'JWT_AUDIENCE': None,
        'JWT_ISSUER': None,

        'JWT_ALLOW_REFRESH': False,
        'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),

        'JWT_AUTH_HEADER_PREFIX': 'JWT',
        'JWT_AUTH_COOKIE': None,

    })

    # Локаль, переменная окружения DJANGO_LANGUAGE_CODE, работате когда USE_I18N=True
    LANGUAGE_CODE = values.Value('ru-ru')

    # Настройки таймзоны, переменная окружения DJANGO_TIME_ZONE
    TIME_ZONE = values.Value('UTC')

    # Использовать локаль, переменная окружения DJANGO_USE_I18N
    USE_I18N = values.BooleanValue(True)

    # Отображение даты и времени в текущей локали, переменная окружения DJANGO_USE_L10N
    USE_L10N = values.BooleanValue(True)

    # Логическое значение, указывающее, будут ли даты по умолчанию учитвать часовой пояс или нет.
    # Переменная окружения DJANGO_USE_TZ
    USE_TZ = values.BooleanValue(True)

    # URL-адрес, который обрабатывает мультимедийные данные, переменная окружения DJANGO_MEDIA_URL
    MEDIA_URL = values.Value('/media/')

    # URL-адрес для использования при обращении к статическим файлам, переменная окружения DJANGO_STATIC_URL
    STATIC_URL = values.Value('/static/')

    # Путь к статическим файлам
    STATIC_ROOT = values.PathValue(os.path.join(BASE_DIR, 'static'), check_exists=False)

    # Путь к мелиа файлам
    MEDIA_ROOT = values.PathValue(os.path.join(BASE_DIR, 'media'), check_exists=False)

    # Путь к файлу с переменными окружения
    DOTENV = os.path.join(BASE_DIR, '.env')

    # Суперюзер базы
    PG_SUPERUSER_NAME = values.Value('task_manager')

    # Пароль суперюзера от базы
    PG_SUPERUSER_PASS = values.Value('secr3t')

    # Список правил для проверки сайтов которым разрешено выполнять межсайтовые запросы
    # Перемнная окружения DJANGO_CORS_ORIGIN_REGEX_WHITELIST
    CORS_ORIGIN_REGEX_WHITELIST = values.ListValue([r'^.*$'])

    # Разрешить включение cookie при запросах
    CORS_ALLOW_CREDENTIALS = values.BooleanValue(True)

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages'
                ],
            },
        },
    ]

    @property
    def IS_DEVELOP(self) -> bool:
        return self.__class__.__name__ == 'Dev'

    @classmethod
    def post_setup(cls) -> None:
        sys.path.insert(0, os.path.join(cls.BASE_DIR, 'apps'))

    @classmethod
    def load_dotenv(cls) -> None:
        try:
            super().load_dotenv()
        except ImproperlyConfigured:
            pass
