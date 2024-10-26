from rest_framework import generics
from core.models import VehicleEngine
from core.serializers import VehicleEngineSerializer

class VehicleEngineListCreateView(generics.ListCreateAPIView):
    queryset = VehicleEngine.objects.all()
    serializer_class = VehicleEngineSerializer

class VehicleEngineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleEngine.objects.all()
    serializer_class = VehicleEngineSerializer
