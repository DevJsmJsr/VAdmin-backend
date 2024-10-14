from django.db import models

from core.models import Auditor


class LocationReference(Auditor):
  code = models.CharField(max_length=100)
  reference = models.CharField(max_length=150)
