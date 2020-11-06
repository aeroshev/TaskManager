from uuid import uuid4

from django.db import models


class Team(models.Model):
    """
    Модель данных команды
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    name = models.CharField(
        max_length=1024,
        help_text='Название команды'
    )  # type: str

    class Meta:
        db_table = 'teams'
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
