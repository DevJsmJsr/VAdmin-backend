from rest_framework import generics
from core.models import Vehicle
from core.serializers import VehicleSerializer

class VehicleAPIView(generics.ListCreateAPIView):
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer