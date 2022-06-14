from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("<a href='about/'>ABOUT</a> <a href='projects/'>PROJECTS</a> <a href='contact/'>CONTACT</a> <h1>I am in the homepage</h1>")


def about(request):
    return HttpResponse("<a href='/'>HOME</a> <a href='/projects/'>PROJECTS</a> <a href='/contact/'>CONTACT</a> <h1>I am in the about page</h1>")


def projects(request):
    return HttpResponse("<a href='/'>HOME</a> <a href='/about/'>ABOUT</a> <a href='/contact/'>CONTACT</a> <h1>I am in the project page</h1>")


def contact(request):
    return HttpResponse("<a href='/'>HOME</a> <a href='/about/'>ABOUT</a> <a href='/projects/'>PROJECTS</a> <h1>I am in the contact page</h1>")
