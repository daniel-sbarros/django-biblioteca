from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from home.forms import LoginForms
from books.models import Book
from rental.models import Rental


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    return redirect('home')

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    data_rentals = Rental.objects.order_by('-rental_date').all()[:10]
    data_books = Book.objects.order_by('-registration_date').all()[:10]
    debitos = Rental.objects.order_by('rental_date').filter(return_period__lt=datetime.now().date())[:5]

    return render(request, 'home/home.html', {'rentals':data_rentals, 'books':data_books, 'debitos':debitos })

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['login_user'].value()
            senha = form['login_password'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Usuário {nome} logado com sucesso.')
                return redirect('home')
            else:
                messages.error(request, f'Erro ao efetuar login.')
                return redirect('login')

    return render(request, 'home/login.html', { 'form':form })

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('login')
