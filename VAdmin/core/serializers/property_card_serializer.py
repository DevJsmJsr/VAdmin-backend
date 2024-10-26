from rest_framework import serializers
from core.models import PropertyCard

from core.serializers import PersonSerializer, VehicleSerializer

class PropertyCardSerializer(serializers.ModelSerializer):
  person = PersonSerializer(read_only=True)
  person_uuid = serializers.UUIDField(write_only=True)
  vehicle = VehicleSerializer(read_only=True)
  vehicle_id = serializers.IntegerField(write_only=True)
  
  class Meta:
    model = PropertyCard
    fields = [
      'property_card_number',
      'issue_date',
      'enrollment_date',
      'transit_authority',
      'person',
      'person_uuid',
      'vehicle',
      'vehicle_id'
    ]