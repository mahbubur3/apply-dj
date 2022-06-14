from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def output(request):
    return render(request, 'myapp/index.html')
