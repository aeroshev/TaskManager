from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import FieldFile


class User(AbstractUser):
    """
    Модель данных пользователей
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    avatar = models.ImageField(
        upload_to='',
        help_text=''
    )  # type: FieldFile

    class Meta:
        db_table = 'tm_users'
        verbose_name = 'Пользователь TM'
        verbose_name_plural = 'Пользователи TM'
