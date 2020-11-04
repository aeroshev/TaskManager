from django.db import models
from uuid import uuid4

from core.models.statuses import Status
from core.models.projects import Project


class Task(models.Model):
    """
    Модель данных задач проекта
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    status = models.ForeignKey(
        Status,
        related_name='tasks',
        on_delete=models.SET_NULL,
        help_text='Ссылка на тип задания'
    )
    project = models.ForeignKey(
        Project,
        related_name='tasks',
        on_delete=models.CASCADE,
        help_text='Ссылка на проект'
    )
    previous_task = models.OneToOneField(

    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
