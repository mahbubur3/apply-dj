from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def output(request):
    return HttpResponse("<h1>I am from algorithom</h1>")
