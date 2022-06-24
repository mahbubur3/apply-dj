from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Student
from MyApp import forms


def home(request):
    students = Student.objects.order_by('name')
    data = {'students': students}
    return render(request, 'myapp/home.html', context=data)


def form(request):
    student_form = forms.StudentForm()

    if request.method == 'POST':
        student_form = forms.StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save(commit=True)
            return home(request)

    data = {'student_form': student_form}

    return render(request, 'myapp/form.html', context=data)
