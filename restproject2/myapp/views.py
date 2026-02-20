from django.shortcuts import render
from myapp.serializers import EmployeeSerializers
from myapp.models import Employee
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class EmployeeViewSet(ModelViewSet):
       queryset=Employee.objects.all()
       serializer_class=EmployeeSerializers         