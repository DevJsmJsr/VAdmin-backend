from rest_framework import serializers
from core.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vehicle
    fields = ['number_plate', 'model', 'brand', 'color', 'doors_number', 'fuel_type', 'kilometric']
