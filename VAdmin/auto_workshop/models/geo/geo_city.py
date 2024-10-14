from django.db import models

from core.models.auditor import Auditor
from core.models.geo.geo_state import GeoState


class GeoCity(Auditor):
  id = models.CharField(primary_key=True, max_length=50)
  name = models.CharField(max_length=150)
  geo_state = models.ForeignKey(GeoState, on_delete=models.CASCADE)
  dane_code = models.CharField(max_length=150, null=True)
  homologate_code = models.CharField(max_length=150, null=True)