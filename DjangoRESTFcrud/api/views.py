from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializers import StudentSerializer


# show all data 
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


# show single student data 
@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)


# add student
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# add student
@api_view(['POST'])
def update_student(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# delete student
@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response('deleted')

