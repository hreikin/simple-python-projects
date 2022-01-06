from django.contrib import admin
# Import created models.
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.

# Define inline Book class so it is linked/viewable on a authors's detail 
# view page.
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class.
class AuthorAdmin(admin.ModelAdmin):
    # Defines which fields are shown when viewing the list of authors in the 
    # admin site.
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


    # Defines how to show the fields inside the admin interface when viewing an 
    # author. When grouped in brackets they will show on the same row. Fieldsets 
    # can be used instead of fields to group the information together.
    # 
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    fieldsets = (
        ('Details', {
            'fields': ('last_name', 'first_name', ('date_of_birth', 'date_of_death'))
        }),
    )

    inlines = [BookInline]

# Register the admin class with the associated model.
admin.site.register(Author, AuthorAdmin)

# Define inline BookInstance class so it is linked/viewable on a book's detail 
# view page.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator, this does the same as 
# the admin.site.register() syntax
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'genre')
    list_display = ('title', 'author', 'display_genre')
    fieldsets = (
        ('Details', {
            'fields': ('title', 'author', 'summary', 'genre', 'isbn', 'language')
        }),
    )

    inlines = [BookInstanceInline]

# Register the Admin classes for BookInstance using the decorator.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
    fieldsets = (
        ('Details', {
            'fields': ('id', 'book', 'imprint')
        }),
        ('Availability', {
            'fields': ('due_back', 'status')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)