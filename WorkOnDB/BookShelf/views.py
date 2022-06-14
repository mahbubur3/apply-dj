from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2>Hello there, I'm in the homepage.</h2>")


def about(request):
    return HttpResponse("<h2>Hey, This is about page.</h2>")


def contact(request):
    return HttpResponse("<h2>Hey, This is contact page.</h2>")
