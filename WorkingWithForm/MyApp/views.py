from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms


def home(request):
    return render(request, 'myapp/index.html')


def form(request):
    form = forms.NameForm()
    info = {
        "my_form": form
    }
    return render(request, 'myapp/form.html', context=info)
