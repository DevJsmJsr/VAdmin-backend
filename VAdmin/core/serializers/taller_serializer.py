from rest_framework import serializers
from core.models import Taller

class TallerSerializer(serializers.Serializer):
  class Meta:
    model = Taller
    fields = ['name','phone','id']
    datatables_always_serialize = fields