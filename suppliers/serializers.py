from rest_framework import serializers

from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для поставщика."""

    class Meta:
        model = Supplier
        fields = ('id', 'network_name', 'supplier', 'hierarchy_level', 'debt',
                  'created_at',)
        read_only_fields = ('debt', 'created_at',)


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
