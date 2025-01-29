from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    """Сериализатор продукта."""

    class Meta:
        model = Product
        fields = ('supplier', 'title', 'model', 'price', 'description',
                  'release_date', 'image',)


class ProductDetailSerializer(ModelSerializer):
    """Сериализатор просмотра одного продукта."""

    class Meta:
        model = Product
        fields = ('title', 'model', 'price', 'description', 'release_date',
                  'image',)
