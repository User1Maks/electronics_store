from django.db import models

from contacts.models import Contact
from products.models import Product

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
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE,
                                   verbose_name='Контакт',
                                   related_name='supplier_contact')
    product = models.ManyToManyField(Product, related_name='suppliers',
                                     verbose_name='Продукт')
    supplier = models.ForeignKey(
        'suppliers.Supplier',
        **NULLABLE,
        verbose_name='Поставщик',
        on_delete=models.SET_NULL,
        related_name='clients'
    )
    debt = models.DecimalField(**NULLABLE,
                               max_digits=12, decimal_places=2,
                               verbose_name='Долг перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания',
                                      editable=False)
