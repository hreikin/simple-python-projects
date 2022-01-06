from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Author, Book, BookInstance, Genre, Language

def index(request):
    """View function for home page of site."""

    # Generate counts for some of the main objects.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a').
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Amount of genres.
    num_genres = Genre.objects.count()

    # Number of books with Python in the title.
    num_python = Book.objects.filter(title__contains='python').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_python': num_python
    }

    # Render the HTML template index.html with the data held in the context 
    # variable.
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book