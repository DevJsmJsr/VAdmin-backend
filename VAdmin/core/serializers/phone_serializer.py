from rest_framework import serializers
from core.models import Phone

class PhoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phone
    fields = ['id', 'phone_number']