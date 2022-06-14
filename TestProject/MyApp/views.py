from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<a href="about/">about</a> <a href="contact/">contact</a> <h2>Hi, this is homepage</h2>')


def about(request):
    return HttpResponse('<a href="/">home</a> <a href="/contact/">contact</a> <h2>Hi, this is about page</h2>')


def contact(request):
    return HttpResponse('<a href="/">home</a> <a href="/about/">about</a> <h2>Hi, this is contact page</h2>')
