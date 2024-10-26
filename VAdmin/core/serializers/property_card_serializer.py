from rest_framework import serializers
from core.models import PropertyCard

from django.utils.module_loading import import_string

class PropertyCardSerializer(serializers.ModelSerializer):
  person = serializers.PrimaryKeyRelatedField(read_only=True)
  person_uuid = serializers.UUIDField(write_only=True)
  vehicle = serializers.PrimaryKeyRelatedField(read_only=True)
  vehicle_id = serializers.IntegerField(write_only=True)
  
  class Meta:
    model = import_string('core.models.PropertyCard')
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