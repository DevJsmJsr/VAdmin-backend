from rest_framework import serializers
from core.models import VehicleAccessories

class VehicleAccessoriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = VehicleAccessories
    fields = '__all__'
