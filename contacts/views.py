from rest_framework import viewsets

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactViewSet(viewsets.ViewSet):
    """ViewSet для контактов."""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
