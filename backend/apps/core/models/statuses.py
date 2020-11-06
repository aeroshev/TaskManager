from django.db import models


class Status(models.Model):
    """
    Модель данных статуса задания
    """
    description = models.CharField(
        max_length=1024,
        help_text='Описание типа задания'
    )

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задачи'
