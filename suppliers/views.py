from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import views

from suppliers.models import Supplier
from suppliers.paginators import SuppliersPermission
from suppliers.serializers import AddProductSerializer, SupplierSerializer
from suppliers.services import add_product_to_supplier
from users.permissions import IsActive
from django.core.exceptions import ObjectDoesNotExist


class SupplierCreateAPIView(generics.CreateAPIView):
    """Endpoint добавления поставщика."""
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierListAPIView(generics.ListAPIView):
    """Endpoint списка поставщиков."""
    queryset = Supplier.objects.all().order_by('-created_at')
    serializer_class = SupplierSerializer
    pagination_class = SuppliersPermission
    permission_classes = [IsActive]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """Endpoint просмотра поставщика."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """Endpoint обновления поставщика."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """Endpoint удаления поставщика."""
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]


class AddProductView(views.APIView):
    """
    Представление для добавления продукта поставщику и обновления задолженности.
    """
    permission_classes = [IsActive]

    def post(self, request):
        """
        Обрабатывает POST-запрос для добавления продукта поставщику, а
        также обновляет его долг перед поставщиком у которого, закупил продукт.
        """
        serializer = AddProductSerializer(data=request.data)

        if serializer.is_valid():

            client_id = serializer.validated_data['client_id']
            supplier_id = serializer.validated_data['supplier_id']
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            try:
                add_product_to_supplier(client_id, supplier_id, product_id,
                                        quantity)
                return Response({'message': 'Продукт успешно добавлен и долг'
                                            'обновлен'},
                                status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({'error': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return Response({'error': 'Указанные объекты не найдены.'})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
