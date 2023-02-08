from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_date(request, date):
    template = 'books/books_list.html'

    books_filter = Book.objects.filter(pub_date=date)
    previous_p = Book.objects.filter(pub_date__lt=date).order_by('pub_date')
    next_p = Book.objects.filter(pub_date__gt=date).order_by('pub_date')

    if len(previous_p) != 0:
        previous_page = previous_p.last().pub_date.strftime("%Y-%m-%d")
    else:
        previous_page = None

    if len(next_p) != 0:
        next_page = next_p.first().pub_date.strftime("%Y-%m-%d")
    else:
        next_page = None

    context = {'books': books_filter,
               'previous_page': previous_page,
               'next_page': next_page,
               }
    return render(request, template, context)

