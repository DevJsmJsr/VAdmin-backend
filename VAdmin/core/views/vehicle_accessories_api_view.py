from rest_framework import generics
from core.models import VehicleAccessories
from core.serializers import VehicleAccessoriesSerializer

class VehicleAccessoriesListCreateView(generics.ListCreateAPIView):
  queryset = VehicleAccessories.objects.all()
  serializer_class = VehicleAccessoriesSerializer

class VehicleAccessoriesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = VehicleAccessories.objects.all()
  serializer_class = VehicleAccessoriesSerializer
