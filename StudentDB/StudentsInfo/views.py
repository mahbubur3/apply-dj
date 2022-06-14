from django.shortcuts import render
from django.http import HttpResponse
from StudentsInfo.models import Student


def home(request):
    students = Student.objects.order_by('name')
    data = {
        "university_name": "University of Toronto",
        "students": students
    }
    return render(request, 'StudentsInfo/index.html', context=data)
