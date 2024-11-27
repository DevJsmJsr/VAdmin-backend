from rest_framework import serializers
from core.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
  doors_number = serializers.CharField(required=False)
  kilometric = serializers.CharField(required=False)
  property_card_id = serializers.IntegerField(write_only=True)
  class Meta:
    model = Vehicle
    fields = ['number_plate', 'model', 'brand', 'type_vehicle',
              'color', 'doors_number', 'fuel_type', 'kilometric',
              'property_card_id']
