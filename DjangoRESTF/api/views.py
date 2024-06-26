from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def show_data(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)