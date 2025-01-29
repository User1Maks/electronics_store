from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from suppliers.models import Supplier


class Contact(models.Model):
    """Модель контакта."""
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE,
                                    verbose_name='Поставщик',
                                    related_name='contacts')
    email = models.EmailField(unique=True, verbose_name='Email',
                              help_text='Укажите email')
    country = models.CharField(max_length=100,
                               verbose_name='Страна',
                               help_text='Укажите страну')
    city = models.CharField(max_length=100, verbose_name='Город',
                            help_text='Укажите город')
    street = models.CharField(max_length=100, verbose_name='Улица',
                              help_text='Укажите название улицы')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома',
                                    help_text='Укажите номер дома')
    phone = PhoneNumberField(blank=True, null=True,
                             verbose_name='Номер телефона',
                             help_text='Введите номер телефона',
                             unique=True)

    def __str__(self):
        return f'{self.email}'

    class Metta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
