from django.shortcuts import render
from .models import Student
from .serilazers import StudentSerlazers
from rest_framework import viewsets


# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerlazers

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerlazers

