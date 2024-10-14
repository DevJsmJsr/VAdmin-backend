from django_filters import rest_framework as filters
from rest_framework import generics
from core.models import Person
from core.serializers import PersonSerializer

class PersonListAPIView(
  generics.ListCreateAPIView
):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
