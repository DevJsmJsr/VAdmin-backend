from rest_framework import serializers
from core.models import PropertyCard

class PropertyCardSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyCard
    fields = ['expiration_date', 'matriculation_date', 'person_uuid', 'vehicle_id']