from django.urls import path
from rental.views import rental, rentals

urlpatterns = [
    path('rentals', rentals, name='rentals'),
    path('rental/<int:rental_id>', rental, name='rental'),
]
