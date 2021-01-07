from configurations import values

from backend.settings.base import Base


class Dev(Base):
    """
    Настройки приложения для разработки
    """
    # Режим приложения для разработки
    DEBUG = values.BooleanValue(True)

    INSTALLED_APPS = values.ListValue([
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework.authtoken',
        'corsheaders',
        'api',
        'core'
    ])

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
