from rest_framework import serializers
from core.models import Garage

class GarageSerializer(serializers.Serializer):
  class Meta:
    model = Garage
    fields = ['name','phone','id']
    datatables_always_serialize = fields