from rest_framework import serializers
from core.models import Vehicle
from core.serializers.property_card_serializer import PropertyCardSerializer
from core.serializers.vehicle_accessories_serializer import VehicleAccessoriesSerializer
from core.serializers.vehicle_engine_serializer import VehicleEngineSerializer


class VehicleSerializer(serializers.ModelSerializer):
  doors_number = serializers.CharField(required=False)
  kilometric = serializers.CharField(required=False)
  property_card_id = serializers.IntegerField(write_only=True)
  property_card = PropertyCardSerializer(required=False)
  vehicle_accessories = VehicleAccessoriesSerializer(required=False)
  vehicle_engine = VehicleEngineSerializer(required=False)
  
  class Meta:
    model = Vehicle
    fields = ['number_plate', 'model', 'brand', 'type_vehicle',
              'color', 'doors_number', 'fuel_type', 'kilometric',
              'property_card_id', 'property_card','vehicle_accessories',
              'vehicle_engine','initial_scan']
