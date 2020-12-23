from django.http import HttpRequest

from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    Отключаем проверку CSRF для API
    """
    def enforce_csrf(self, request: HttpRequest) -> None:
        return None
