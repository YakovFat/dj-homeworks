from django.views import generic
from books.models import Book


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
        if self.kwargs:
            curdate = self.kwargs['pub_date']
            previous_object = Book.objects.order_by('pub_date').filter(pub_date__lt=curdate).last()
            if previous_object:
                previous_date = str(previous_object.pub_date)
                context['previous_date'] = previous_date
            next_object = Book.objects.order_by('pub_date').filter(pub_date__gt=curdate).first()
            if next_object:
                next_date = str(next_object.pub_date)
                context['next_date'] = next_date
        return context

