from django.shortcuts import redirect, render
from django.contrib import messages


def users(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    return render(request, 'users/index.html')