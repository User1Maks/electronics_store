from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date',)
    list_filter = ('supplier__contacts__country', 'supplier',)
    search_fields = ('title', 'model',)
