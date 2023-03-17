from django.urls import path
from books.views import books
# from galeria.views import buscar, index, imagem

urlpatterns = [
    # path('', index, name='index'),
    # path('imagem/<int:foto_id>', imagem, name='imagem'),
    # path('buscar', buscar, name='buscar')
    path('books', books, name='books'),
]