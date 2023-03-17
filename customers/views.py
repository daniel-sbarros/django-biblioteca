from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from customers.atraso import Atraso
from customers.models import Customer
from rental.models import Rental
from django.db.models import Q


def customers(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    return render(request, 'customers/index.html')

def customer(request, customer_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    customer = get_object_or_404(Customer, pk=customer_id)

    debitos = Rental.objects.order_by('-rental_date').filter(
        Q(return_period__lt=datetime.now().date()) & Q(delivered=False) & Q(rental_customer=customer_id)
    )

    dados = []
    for debito in debitos:
        dados.append(Atraso(debito))
        
    alugueis = Rental.objects.order_by('-rental_date').filter(rental_customer=customer_id)
            
    return render(request, 'customers/customer.html', { 'customer':customer, 'dados':dados, 'alugueis':alugueis })

