from django.contrib import admin
from books.models import Book

class ListBooks(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'release_year', 'registration_user')
    list_display_links = ('id', 'title', 'author', 'category', 'release_year', 'registration_user')
    search_fields = ('title',)
    list_filter = ("author", 'category',)
    list_per_page = 10

admin.site.register(Book, ListBooks)
