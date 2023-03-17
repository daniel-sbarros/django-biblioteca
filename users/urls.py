from django.urls import path
from users.views import users


urlpatterns = [
    # path('', index, name='index'),
    # path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('users', users, name='users')
    
]