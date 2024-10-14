from django.db import models

from core.models import Auditor
from core.models import GeoCity
from core.models import GeoState
from core.models import Reference
from core.models import Garage


class Location(Auditor):
  address = models.TextField()
  suggested_address = models.TextField(null=True)
  latitude = models.DecimalField(max_digits=23, decimal_places=20, null=True)
  longitude = models.DecimalField(max_digits=23, decimal_places=20, null=True)
  description_value = models.CharField(max_length=70, null=True)
  description_number = models.CharField(max_length=70, null=True)
  description_consecutive = models.CharField(max_length=70, null=True)
  observation = models.TextField(null=True)
  reference = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)
  geo_city = models.ForeignKey(GeoCity, on_delete=models.CASCADE, null=True)
  geo_state = models.ForeignKey(GeoState, on_delete=models.CASCADE, null=True)
  garage = models.ForeignKey(
    Garage, on_delete=models.CASCADE, related_name='garage_location'
  )
