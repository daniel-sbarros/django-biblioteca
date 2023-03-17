from django.urls import path
from customers.views import customer, customers

urlpatterns = [
    path('customers', customers, name='customers'),
    path('customer/<int:customer_id>', customer, name='customer'),
]
