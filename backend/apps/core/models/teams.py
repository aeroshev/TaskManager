from django.db import models
from uuid import uuid4


class Team(models.Model):
    """
    Модель данных команды
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str

    class Meta:
        db_table = 'teams'
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
