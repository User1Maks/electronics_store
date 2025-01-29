from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'email', 'country', 'city', 'street',
                    'house_number', 'phone',)
    list_filter = ('country', 'city',)
    search_fields = ('supplier__network_name', 'email',)
