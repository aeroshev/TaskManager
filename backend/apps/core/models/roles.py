from uuid import uuid4

from django.db import models


class Role(models.Model):
    """
    Модель данных роли участника в команде
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    description = models.CharField(
        max_length=1024,
        help_text='Описание роли'
    )  # type: str

    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль участника'
        verbose_name_plural = 'Роли участника'
