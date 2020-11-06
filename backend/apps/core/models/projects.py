from uuid import uuid4

from django.db import models
from django.db.models.fields.files import FieldFile

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
    product_name = models.CharField(
        max_length=512,
        help_text='Имя продукта'
    )  # type: str
    team = models.ForeignKey(
        Team,
        related_name='projects',
        on_delete=models.PROTECT,
        help_text='Ссылка на команду проекта'
    )
    docs = models.FileField(
        upload_to='',
        help_text=''
    )  # type: FieldFile

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
