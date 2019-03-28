from django.views import generic
from books.models import Book
from django.shortcuts import get_object_or_404


class BookListView(generic.ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

    def get_queryset(self):
        if self.kwargs:
            qs = Book.objects.filter(pub_date=self.kwargs['pub_date'])
            return qs
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

