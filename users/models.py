from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from suppliers.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(max_length=50,
                                verbose_name='Никнейм пользователя',
                                unique=True,
                                help_text='Введите имя пользователя'
                                )
    email = models.EmailField(unique=True, verbose_name='Email',
                              **NULLABLE,
                              help_text='Укажите email')
    first_name = models.CharField(max_length=50,
                                  **NULLABLE,
                                  verbose_name='Имя',
                                  help_text='Введите имя')
    last_name = models.CharField(max_length=50,
                                 **NULLABLE,
                                 verbose_name='Фамилия',
                                 help_text='Введите фамилию')
    phone = PhoneNumberField(verbose_name='Номер телефона',
                             **NULLABLE,
                             help_text='Введите номер телефона',
                             unique=True)
    avatar = models.ImageField(upload_to='users/avatars/',
                               verbose_name='Аватар',
                               **NULLABLE,
                               help_text='Загрузите аватар профиля')
    date_of_birth = models.DateField(verbose_name='Дата рождения',
                                     **NULLABLE,
                                     help_text='Введите дату рождения')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
