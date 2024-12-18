from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
