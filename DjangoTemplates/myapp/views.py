from django.shortcuts import render
from django.http import HttpResponse

# Create your views here


def show(request):
    info = {
        "brand": "Corsair",
        "nationality": "American",
        "born": 1994

    }
    return render(request, 'myapp/index.html', context=info)
