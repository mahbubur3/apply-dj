from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    person_info = {
        'name': 'Holy Dalton',
        'id': 98
    }
    return render(request, 'myapp/index.html', context=person_info)
