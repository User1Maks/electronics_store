from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import SupplierContactsSerializer
from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для поставщика."""
    contacts = SupplierContactsSerializer(required=False)

    class Meta:
        model = Supplier
        fields = ('id', 'network_name', 'supplier', 'hierarchy_level', 'debt',
                  'created_at', 'contacts',)
        read_only_fields = ('debt', 'created_at',)

    def validate(self, data):
        """Валидация данных модели Supplier."""
        supplier = data.get('supplier')

        # Логика для автоматического вычисления hierarchy_level
        if supplier is None:
            data['hierarchy_level'] = 0
        elif supplier.hierarchy_level == 0:
            data['hierarchy_level'] = 1
        else:
            data['hierarchy_level'] = 2

        return data

    def create(self, validated_data):
        """Добавляет контакты для поставщика."""
        contact_data = validated_data.pop('contacts', None)
        supplier = Supplier.objects.create(**validated_data)

        if contact_data:
            Contact.objects.create(supplier=supplier, **contact_data)
        return supplier

    def update(self, instance, validated_data):
        """Обновляет данные контактов для поставщика."""
        contacts_data = validated_data.pop('contacts', None)

        instance.network_name = validated_data.get(
            'network_name', instance.network_name)
        instance.supplier = validated_data.get(
            'supplier', instance.supplier)
        instance.save()

        if contacts_data:
            contact, created = Contact.objects.get_or_create(
                supplier=instance)
            for key, value in contacts_data.items():
                setattr(contact, key, value)
            contact.save()

        return instance


class AddProductSerializer(serializers.Serializer):
    """Сериализатор для добавления товара поставщику."""
    client_id = serializers.IntegerField(
        required=True,
        help_text='ID клиента (поставщика, который заказывает продукт).')
    supplier_id = serializers.IntegerField(
        required=True,
        help_text='ID поставщика, у которого заказывают продукт.')
    product_id = serializers.IntegerField(
        required=True,
        help_text='ID продукта.')
    quantity = serializers.IntegerField(
        required=True, min_value=1,
        help_text='Количество продукта.')

