from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import (SupplierCreateAPIView, SupplierDestroyAPIView,
                             SupplierListAPIView, SupplierRetrieveAPIView,
                             SupplierUpdateAPIView)

app_name = SuppliersConfig.name

urlpatterns = [
    path('create/', SupplierCreateAPIView.as_view(), name='supplier_create'),
    path('list/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('detail/<int:pk>/', SupplierRetrieveAPIView.as_view(),
         name='supplier_detail'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(),
         name='supplier_update'),
    path('delete/<int:pk>/', SupplierDestroyAPIView.as_view(),
         name='supplier_delete'),

]
