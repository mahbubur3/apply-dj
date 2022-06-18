from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms


def home(request):
    return render(request, 'myapp/index.html')


def form(request):
    form = forms.InfoForm()
    data = {
        'heading': 'Please fill up this form.',
        'form': form,
    }

    if request.method == 'POST':
        form = forms.InfoForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']

            data.update({'name': name})
            data.update({'email': email})
            data.update({'dob': dob})
            data.update({'address': address})
            data.update({'submited': 'Yes.'})

    return render(request, 'myapp/form.html', context=data)
