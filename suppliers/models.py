from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Supplier(models.Model):
    """Модель поставщика."""
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    ]
    network_name = models.CharField(max_length=200,
                                    verbose_name='Название поставщика',
                                    help_text='Введите название поставщика')
    supplier = models.ForeignKey(
        'self',
        **NULLABLE,
        verbose_name='Поставщик',
        help_text='Поставщик, который закупает товар у другого поставщика',
        on_delete=models.SET_NULL,
        related_name='client'
    )
    hierarchy_level = models.IntegerField(
        choices=LEVEL_CHOICES,
        verbose_name='Уровень иерархии',
        help_text='Уровень иерархии поставщика'
    )

    debt = models.DecimalField(max_digits=12, decimal_places=2,
                               verbose_name='Долг перед поставщиком',
                               editable=False, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания',
                                      editable=False)

    def __str__(self):
        return f'{self.network_name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
