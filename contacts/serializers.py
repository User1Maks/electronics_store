from rest_framework.serializers import ModelSerializer

from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    """Сериализатор контакта."""
    class Meta:
        model = Contact
        fields = '__all__'
