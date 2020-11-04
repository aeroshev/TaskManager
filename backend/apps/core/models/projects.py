from django.db import models
from uuid import uuid4

from core.models.teams import Team


class Project(models.Model):
    """
    Модель данных проекта
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    description = models.CharField(
        max_length=1024,
        help_text='Описание проекта'
    )  # type: str
    team = models.ForeignKey(
        Team,
        related_name='projects',
        on_delete=mdoels.PROTECT,
        help_text='Ссылка на команду проекта'
    )

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
