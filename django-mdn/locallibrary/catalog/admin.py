from django.contrib import admin
# Import created models.
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)