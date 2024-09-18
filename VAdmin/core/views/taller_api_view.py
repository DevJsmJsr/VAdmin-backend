from rest_framework import generics
from core.serializers import TallerSerializer
from core.models import Taller

class TallerAPIView(generics.ListCreateAPIView):
  serializer_class = TallerSerializer
  queryset = Taller.objects.all().order_by('name')
  