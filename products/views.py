from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from products.models import Product
from products.paginators import ProductPaginator
from products.serializers import ProductDetailSerializer, ProductSerializer
from users.permissions import IsActive


class ProductCreateAPIView(generics.CreateAPIView):
    """Endpoint создания продукта."""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]

    def perform_create(self, serializer):
        """Автоматически добавляет пользователя добавившего продукт."""
        serializer.save(created_by=self.request.user)


class ProductListAPIView(generics.ListAPIView):
    """Endpoint просмотра списка продуктов."""
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    pagination_class = ProductPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('price',)
    ordering_fields = ('title', 'release_date',)
    search_fields = ('title', 'model',)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Endpoint просмотра продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Endpoint обновления продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsActive]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Endpoint для удаления продукта."""
    queryset = Product.objects.all()
    permission_classes = [IsActive]
