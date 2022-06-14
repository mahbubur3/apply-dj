from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Product


def home(request):
    my_orders = Product.objects.order_by('name')
    info = {
        'name': 'Mahbubur Rahman',
        'profession': 'Student',
        'my_orders': my_orders,
    }

    return render(request, 'myapp/index.html', context=info)
