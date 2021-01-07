from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.fields.files import FieldFile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class UserManager(BaseUserManager):
    """
    Кастомный менеджер управления моделями User
    """
    def create_user(self, email: str, username: str, password: str) -> 'TMAbstractUser':
        if not email:
            raise ValueError("Users must have an email address")
        elif not username:
            raise ValueError("Users must have a username")
        elif password is None:
            raise TypeError('Users must have a password.')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, username: str, password: str) -> 'TMAbstractUser':
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class TMAbstractUser(AbstractBaseUser):
    """
    Кастомная абстрактная модель пользователя
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    email = models.EmailField(
        verbose_name='Email адреса',
        max_length=255,
        unique=True,
        help_text='Электронная почта пользователя'
    )  # type: models.EmailField
    username = models.CharField(
        max_length=64,
        unique=True,
        help_text='Имя пользователя'
    )  # type: str
    is_active = models.BooleanField(
        default=True,
        help_text='Активный статус пользователя'
    )  # type: bool
    is_staff = models.BooleanField(
        default=False,
        help_text='Служебный статус'
    )  # type: bool
    is_superuser = models.BooleanField(
        default=False,
        help_text='Суперпользователь'
    )  # type: bool
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tm_users'
        verbose_name = 'Пользователь TM'
        verbose_name_plural = 'Пользователи TM'


class TMUser(models.Model):
    """
    Полная модель пользователя
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )  # type: str
    user = models.OneToOneField(
        TMAbstractUser,
        on_delete=models.CASCADE,
        related_name='tm_user',
        help_text='Базовое представление пользователя'
    )  # type: str
    avatar = models.ImageField(
        upload_to='',
        help_text='Аватар пользователя'
    )  # type: FieldFile
    first_name = models.CharField(
        max_length=64,
        help_text='Имя пользователя'
    )  # type: str
    last_name = models.CharField(
        max_length=64,
        help_text='Фамилия Пользователя'
    )  # type: str
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        help_text='Телефонный номер пользователя'
    )  # type: str
    age = models.PositiveSmallIntegerField(
        null=True,
        help_text='Возраст пользователя'
    )  # type: int
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        help_text='Гендер пользователя'
    )  # type: str

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'tm_profile'
        verbose_name = 'Профиль пользователя ТМ'
        verbose_name_plural = 'Профиль пользователей ТМ'
