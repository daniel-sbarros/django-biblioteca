from django.contrib import admin
from rental.models import Rental

class ListRental(admin.ModelAdmin):
    list_display = ('id', 'rental_customer', 'rental_book', 'return_period', 'amount_paid')
    list_display_links = ('id', 'rental_customer', 'rental_book', 'return_period',)
    search_fields = ('rental_book__title', 'rental_customer__name')
    list_editable = ('amount_paid',)
    list_filter = ("rental_customer", 'return_period')
    list_per_page = 20

admin.site.register(Rental, ListRental)
