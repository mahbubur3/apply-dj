from django.shortcuts import render
from django.http import HttpResponse
from YourApp.models import Car
from YourApp import forms


def index(request):
    cars = Car.objects.order_by('brand')
    data = {'cars': cars}
    return render(request, 'yourapp/index.html', context=data)


def form(request):
    my_form = forms.CarForm()

    if request.method == 'POST':
        my_form = forms.CarForm(request.POST)

        if my_form.is_valid():
            my_form.save(commit=True)
            return index(request)

    data = {'my_form': my_form}

    return render(request, 'yourapp/form.html', context=data)
