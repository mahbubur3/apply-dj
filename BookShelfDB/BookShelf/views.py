from django.shortcuts import render
from django.http import HttpResponse
from BookShelf.models import Book


def home(request):
    # SELECT * FROM Book ORDER BY name
    my_books = Book.objects.order_by('name')

    info = {"name": "Mahbub", "my_books": my_books}
    return render(request, 'BookShelf/index.html', context=info)
