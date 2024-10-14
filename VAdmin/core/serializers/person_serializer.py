from rest_framework import serializers
from core.models import Person

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ['first_name', 'second_name', 'first_lastname', 'second_lastname', 'uuid', 'user']