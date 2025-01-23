from rest_framework import generics

from suppliers.models import Supplier
from suppliers.paginators import SuppliersPermission
from suppliers.serializers import SupplierSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """Endpoint добавления поставщика."""
    serializer_class = SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    """Endpoint списка поставщиков."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SuppliersPermission


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """Endpoint просмотра поставщика."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """Endpoint обновления поставщика."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """Endpoint удаления поставщика."""
    queryset = Supplier.objects.all()
