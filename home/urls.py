from django.urls import path
from home.views import home, index, login, logout

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]