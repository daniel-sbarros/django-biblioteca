from django.shortcuts import redirect, render
from django.contrib import messages


def books(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    return render(request, 'books/index.html')

    # dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    # return render(request, 'galeria/index.html', {"cards":dados})