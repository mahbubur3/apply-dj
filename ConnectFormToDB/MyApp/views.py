from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms
from MyApp.models import Book


def home(request):
    books = Book.objects.order_by('book_name')
    data = {'books': books}
    return render(request, 'myapp/index.html', context=data)


def form(request):
    new_form = forms.BookForm()

    if request.method == 'POST':
        new_form = forms.BookForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)

    data = {
        'form': new_form,
        'heading': 'Add a new book.'
    }

    return render(request, 'myapp/form.html', context=data)
