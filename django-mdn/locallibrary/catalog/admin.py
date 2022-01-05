from django.contrib import admin
# Import created models.
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.

# Define the admin class.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model.
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator, this does the same as 
# the admin.site.register() syntax
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'genre')
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator.
# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back')

admin.site.register(Genre)
admin.site.register(Language)