from django.db import models
from uuid import uuid4


class User(models.Model):
    """
    Модель данных пользователей
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    username = models.CharField(
        max_length=64,
        unqiue=True,
        verbose_name='логин',
        help_text='логин пользователя'
    )  # type: str

    class Meta:
        db_table = 'tm_users'
        verbose_name = 'Пользователь TM'
        verbose_name_plural = 'Пользователи TM'
