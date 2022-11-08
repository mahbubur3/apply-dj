from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('homepage..')


def works(request):
    return HttpResponse('your works..')


# pk er jaygay onno nam o deya jay
def work(request, pk): 
    return HttpResponse('single work' + ' ' + str(pk))