from rest_framework import generics
from core.models import PropertyCard
from core.serializers import PropertyCardSerializer

class PropertyCardAPIView(generics.ListCreateAPIView):
  queryset = PropertyCard.objects.all()
  serializer_class = PropertyCardSerializer