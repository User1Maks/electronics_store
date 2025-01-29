from django.contrib import admin

from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'network_name', 'supplier', 'hierarchy_level', 'debt',
                    'created_at',)
    list_filter = ('hierarchy_level', 'contacts__city', 'contacts__country',)
    search_fields = ('network_name',)
    actions = ('clear_debt',)

    @admin.action(description='Очистить задолженность')
    def clear_debt(self, request, queryset):
        """Admin Action для обнуления задолженности у поставщиков."""
        queryset.update(debt=0.00)
