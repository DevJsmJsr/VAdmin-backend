from django.db import models
from core.models import Auditor
from core.models import Person
import uuid

class PropertyCard(Auditor):
  expiration_date = models.DateField()
  matriculation_date = models.DateField()
  person_uuid = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_property_cards')
  vehicle_id = models.OneToOneField('core.Vehicle', on_delete=models.CASCADE, related_name='vehicle_property_cards')
  #todo campos de la tarjeta de propiedad