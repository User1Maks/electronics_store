# Generated by Django 5.1.5 on 2025-01-19 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(help_text='Введите название поставщика', max_length=200, verbose_name='Название поставщика')),
                ('level', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], help_text='Выберите поставщика', verbose_name='Уровень иерархии')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=12, null=True, verbose_name='Долг перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='suppliers.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]
