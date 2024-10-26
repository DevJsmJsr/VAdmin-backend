from rest_framework import serializers
from core.models import VehicleEngine

class VehicleEngineSerializer(serializers.ModelSerializer):
  class Meta:
    model = VehicleEngine
    fields = '__all__'
