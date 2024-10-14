from rest_framework import serializers
from core.models import AutoWorkshop

class AutoWorkshopSerializer(serializers.Serializer):
  class Meta:
    model = AutoWorkshop
    fields = ['name','phone','id']
    datatables_always_serialize = fields