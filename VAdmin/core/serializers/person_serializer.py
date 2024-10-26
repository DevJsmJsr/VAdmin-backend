from rest_framework import serializers
from core.models import Person

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ['uuid','first_name','middle_name','last_name',
              'second_last_name','gender','birth_date',
              'document_number','document_type'
            ]