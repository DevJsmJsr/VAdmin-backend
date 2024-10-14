from rest_framework import generics
from core.serializers import AutoWorkshopSerializer
from core.models import AutoWorkshop

class AutoWorkshopAPIView(generics.ListCreateAPIView):
  serializer_class = AutoWorkshopSerializer
  queryset = AutoWorkshop.objects.all()
  