from django.views import generic
from books.models import Book


class BookListView(generic.ListView):
    model = Book
    def get_context_data(self, **kwargs):
        pass
