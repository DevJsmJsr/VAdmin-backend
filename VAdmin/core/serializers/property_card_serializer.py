from rest_framework import serializers
from core.models import PropertyCard

from core.serializers import PersonSerializer

class PropertyCardSerializer(serializers.ModelSerializer):
  person = PersonSerializer(required=False)
  person_id = serializers.UUIDField(write_only=True)
  issue_date = serializers.CharField(required=False)
  enrollment_date = serializers.CharField(required=False)
  transit_authority = serializers.CharField(required=False)
  pk = serializers.IntegerField(required=False)
  
  class Meta:
    model = PropertyCard
    fields = [
      'pk',
      'property_card_number',
      'issue_date',
      'enrollment_date',
      'transit_authority',
      'person',
      'person_id',
    ]
