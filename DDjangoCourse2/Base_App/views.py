from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('homepage..')


def works(request):
    return render(request, 'BaseApp/works.html')


def work(request): 
    return render(request, 'BaseApp/single-work.html')