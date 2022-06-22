# from django.shortcuts import render
# from django.http import HttpResponse


# def home(request):
#     return HttpResponse('<h1>this is homepage</h1>')


# ------------------

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>i am in the homepage</h1>')
