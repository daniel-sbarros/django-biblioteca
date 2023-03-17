from django.contrib import admin
from customers.models import Customer

class ListCustomer(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'registration_user')
    list_display_links = ('id', 'name', 'email', 'city', 'registration_user')
    search_fields = ('name',)
    list_filter = ("city",)
    list_per_page = 20

admin.site.register(Customer, ListCustomer)
