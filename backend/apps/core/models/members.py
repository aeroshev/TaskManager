from uuid import uuid4

from django.db import models

from core.models.roles import Role
from core.models.task import Task
from core.models.teams import Team
from core.models.users import User


class Member(models.Model):
    """
    Модель данных участников команды
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    user = models.ForeignKey(
        User,
        related_name='members',
        on_delete=models.CASCADE,
        help_text='Ссылка на пользователя'
    )
    role = models.ForeignKey(
        Role,
        related_name='members',
        on_delete=models.PROTECT,
        help_text='Ссылка на роль участника'
    )
    team = models.ForeignKey(
        Team,
        related_name='members',
        on_delete=models.CASCADE,
        help_text='Ссылка на команду участника'
    )
    task = models.ManyToManyField(
        Task,
        related_name='members'
    )

    class Meta:
        db_table = 'members'
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'
        constraints = [
            models.UniqueConstraint(fields=['team', 'role'], name='unique_role_team')
        ]
