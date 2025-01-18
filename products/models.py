from django.db import models


class Product(models.Model):
    """Модель продукта."""
    title = models.CharField(max_length=255, verbose_name='Название продукта',
                             help_text='Введите название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта',
                             help_text='Укажите модель продукта')
    release_date = models.DateField(
        verbose_name='Дата выхода продукта на рынок',
        help_text='Укажите дату выхода продукции на рынок'
    )
    image = models.ImageField(upload_to='products/images/',
                              blank=True, null=True,
                              verbose_name='Изображение продукта',
                              help_text='Загрузите изображение продукта')

    def __str__(self):
        return f'{self.title} {self.model} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
