from rest_framework.serializers import ModelSerializer

from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    """Сериализатор контакта."""
    class Meta:
        model = Contact
        fields = '__all__'


class SupplierContactsSerializer(ModelSerializer):
    """Сериализатор для контактов передаваемых вместе с данными о поставщике."""

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('supplier',)
