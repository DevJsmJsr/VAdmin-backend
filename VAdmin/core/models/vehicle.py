from django.db import models
from core.models import Auditor
from core.models import PropertyCard


class Vehicle(Auditor):
  GAS='GAS'
  DIESEL='DIESEL'
  EXTRA='EXTRA'
  
  FUEL_CHOICES = [
    ('GAS', 'GAS'),
    ('DIESEL', 'DIESEL'),
    ('EXTRA', 'EXTRA'),
  ]
  
  number_plate = models.CharField(max_length=15, unique=True)
  model = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  color = models.CharField(max_length=30)
  type_vehicle = models.CharField(max_length=30)
  doors_number = models.PositiveIntegerField()
  fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
  kilometric = models.PositiveIntegerField()
  property_card = models.OneToOneField(PropertyCard, on_delete=models.CASCADE, related_name='property_cards_vehicle')

