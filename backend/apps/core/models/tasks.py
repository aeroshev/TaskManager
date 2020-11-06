from uuid import uuid4

from django.db import models

from core.models.projects import Project
from core.models.statuses import Status


class Task(models.Model):
    """
    Модель данных задач проекта
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    description = models.CharField(
        max_length=2048,
        help_text='Описание задачи'
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
        'self',
        null=True,
        related_name='next_task',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        constraints = [
            models.UniqueConstraint(fields=['id', 'project'], name='unique_task_project'),
            models.UniqueConstraint(fields=['previous_task'], name='unique_previous_task')
        ]
