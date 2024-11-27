from rest_framework import serializers
from core.models import Person
from core.serializers.user_serializer import UserSerializer

class PersonSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  user_id = serializers.IntegerField(write_only=True)
  gender = serializers.CharField(required=False)
  
  class Meta:
    model = Person
    fields = [
      'uuid','name','gender','birth_date',
      'document_number','document_type',
      'user','user_id'
    ]