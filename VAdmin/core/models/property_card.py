from django.db import models
from core.models import Auditor
from core.models import Person
import uuid

class PropertyCard(Auditor):
  property_card_number = models.CharField(max_length=100, unique=True)
  issue_date = models.DateField()
  enrollment_date = models.DateField()
  transit_authority = models.CharField(max_length=200)
  person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_property_cards')
  vehicle = models.OneToOneField('core.Vehicle', on_delete=models.CASCADE, related_name='vehicle_property_cards')