from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from rental.models import Rental

def rentals(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    alugueis = Rental.objects.all()
    return render(request, 'rental/rentals.html', { 'alugueis':alugueis })

def rental(request, rental_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    aluguel = get_object_or_404(Rental, pk=rental_id)
    return render(request, 'rental/rental.html', { 'aluguel':aluguel })

