from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms


def home(request):
    return render(request, 'myapp/index.html')


# def form(request):
#     form = forms.MyForm()
#     if request.method == 'POST':
#         form = forms.MyForm(request.POST)

#         if form.is_valid():
#             data.update({'field': form.cleaned_data['field']})
#             data.update({'number_field': form.cleaned_data['number_field']})
#             data.update({'submited': 'YES'})

#     data = {
#         'form': form,
#         'heading': 'This is form created by django.'
#     }

#     return render(request, 'myapp/form.html', context=data)


# def form(request):
#     new_form = forms.UserForm()
#     data = {
#         'form': new_form,
#         'heading': 'this is form create using django'
#     }

#     if request.method == 'POST':
#         new_form = forms.UserForm(request.POST)
#         data.update({'form': new_form})

#         if new_form.is_valid():
#             data.update({'field': new_form.cleaned_data['number_field']})
#             data.update({'submited': 'YES'})

#     return render(request, 'myapp/form.html', context=data)


def form(request):
    new_form = forms.UserForm()
    data = {
        'form': new_form,
        'heading': 'this is form create using django'
    }

    if request.method == 'POST':
        new_form = forms.UserForm(request.POST)
        data.update({'form': new_form})

        if new_form.is_valid():
            data.update({'field': 'password match!!'})
            data.update({'submited': 'YES'})

    return render(request, 'myapp/form.html', context=data)
