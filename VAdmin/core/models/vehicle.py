from django.db import models
from core.models import Auditor
from core.models import PropertyCard


class Vehicle(Auditor):
  GASOLINA='GASOLINA'
  DIESEL='DIESEL'
  EXTRA='EXTRA'
  
  FUEL_CHOICES = [
    (GASOLINA, 'GASOLINA'),
    (DIESEL, 'DIESEL'),
    (EXTRA, 'EXTRA'),
  ]
  
  COMPLETED='COMPLETED'
  UNCOMPLETED='UNCOMPLETED'
  
  INITIAL_SCAN_CHOICES = [
    (COMPLETED, 'COMPLETED'),
    (UNCOMPLETED, 'UNCOMPLETED'),
  ]
  
  number_plate = models.CharField(max_length=15, unique=True)
  model = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  color = models.CharField(max_length=30)
  type_vehicle = models.CharField(max_length=30)
  doors_number = models.PositiveIntegerField(null=True)
  fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
  kilometric = models.PositiveIntegerField(null=True)
  initial_scan = models.CharField(max_length=20, default=UNCOMPLETED, choices=INITIAL_SCAN_CHOICES)
  property_card = models.OneToOneField(PropertyCard, on_delete=models.CASCADE, related_name='property_cards_vehicle')

