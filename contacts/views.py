from rest_framework import viewsets

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from users.permissions import IsActive


class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet для контактов."""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('supplier')
    permission_classes = [IsActive]
