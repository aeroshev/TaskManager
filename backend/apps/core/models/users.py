from uuid import uuid4

from django.db import models
from django.db.models.fields.files import FieldFile


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
        unique=True,
        verbose_name='логин',
        help_text='логин пользователя'
    )  # type: str
    real_name = models.CharField(
        max_length=254,
        help_text='реальное имя пользователя'
    )  # type: str
    email = models.EmailField(
        help_text='email пользователя'
    )  # type: str
    avatar = models.ImageField(
        upload_to='',
        help_text=''
    )  # type: FieldFile

    class Meta:
        db_table = 'tm_users'
        verbose_name = 'Пользователь TM'
        verbose_name_plural = 'Пользователи TM'
