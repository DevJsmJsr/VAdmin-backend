from rest_framework import generics
from core.serializers import GarageSerializer
from core.models import Garage

class GarageAPIView(generics.ListCreateAPIView):
  serializer_class = GarageSerializer
  queryset = Garage.objects.all()
  