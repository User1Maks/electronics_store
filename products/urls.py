from django.urls import path

from products.apps import ProductsConfig
from products.views import (ProductCreateAPIView, ProductDestroyAPIView,
                            ProductListAPIView, ProductRetrieveAPIView,
                            ProductUpdateAPIView)

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='products_create'),
    path('list/', ProductListAPIView.as_view(), name='products_list'),
    path('detail/<int:pk>/', ProductRetrieveAPIView.as_view(),
         name='products_detail'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(),
         name='products_update'),
    path('delete/<int:pk>/', ProductDestroyAPIView.as_view(),
         name='products_delete'),

]
