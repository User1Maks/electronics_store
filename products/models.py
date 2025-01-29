from django.db import models

from suppliers.models import NULLABLE, Supplier
from users.models import User


class Product(models.Model):
    """Модель продукта."""
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик',
                                 help_text='Выберите поставщика',
                                 related_name='products',
                                 on_delete=models.CASCADE
                                 )
    title = models.CharField(max_length=255, verbose_name='Название продукта',
                             help_text='Введите название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта',
                             help_text='Укажите модель продукта')
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name='Цена продукта',
                                help_text='Укажите цену продукта')
    description = models.TextField(**NULLABLE,
                                   verbose_name='Описание продукта',
                                   help_text='Введите описание продукта')
    release_date = models.DateField(
        **NULLABLE,
        verbose_name='Дата выхода продукта на рынок',
        help_text='Укажите дату выхода продукции на рынок'
    )
    image = models.ImageField(upload_to='products/images/',
                              **NULLABLE,
                              verbose_name='Изображение продукта',
                              help_text='Загрузите изображение продукта')
    created_by = models.ForeignKey(User, verbose_name='Администратор каталога',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='created_products',
                                   help_text='Пользователь создавший продукт')

    def __str__(self):
        return f'{self.title} {self.model} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
