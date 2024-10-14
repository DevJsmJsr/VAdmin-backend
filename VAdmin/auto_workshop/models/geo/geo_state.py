from django.db import models

from core.models.auditor import Auditor


class GeoState(Auditor):
  id = models.CharField(primary_key=True, max_length=50)
  name = models.CharField(max_length=150)
  dane_code = models.CharField(max_length=150, null=True)
