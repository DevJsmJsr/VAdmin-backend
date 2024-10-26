from rest_framework import serializers
from auto_workshop.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ['id', 'national_id', 'name']