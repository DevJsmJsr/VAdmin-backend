from rest_framework import generics
from auto_workshop.models import Employee
from auto_workshop.serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
