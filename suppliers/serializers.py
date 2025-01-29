from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для поставщика."""
    contacts = ContactSerializer(required=False)

    class Meta:
        model = Supplier
        fields = ('id', 'network_name', 'supplier', 'hierarchy_level', 'debt',
                  'created_at', 'contacts',)
        read_only_fields = ('debt', 'created_at',)

    def validate(self, data):
        """Валидация данных модели Supplier."""
        hierarchy_level = data.get('hierarchy_level')
        supplier = data.get('supplier')

        if hierarchy_level == 0 and supplier is not None:
            raise serializers.ValidationError(
                'Ваш уровень иерархии 0 (Завод), вы не можете '
                'указать поставщика.'
            )

        if hierarchy_level in [1, 2]:

            if supplier is None:
                raise serializers.ValidationError(
                    'Укажите поставщика.'
                )

            if hierarchy_level == 1 and supplier.hierarchy_level != 0:
                raise serializers.ValidationError(
                    'Розничная сеть должна ссылаться на завод.'
                )

            if (hierarchy_level == 2 and supplier.hierarchy_level
                    not in [0, 1]):
                raise serializers.ValidationError(
                    'ИП должен ссылаться на завод или розничную сеть.'
                )

        if self.instance:
            if 'hierarchy_level' in data:
                raise serializers.ValidationError(
                    'Обновление уровня иерархии запрещено, так как оно'
                    'определенно вашим отношением к остальным элементам '
                    'сети.'
                )

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

    def post(self, request):
        serializer = AddProductSerializer(data=request.data)
        if serializer.is_valid():
            print(f"Validated data: {serializer.validated_data}")
