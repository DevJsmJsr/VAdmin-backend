from django.db import models
from django.conf import settings
from core.models import Auditor
import uuid

class Person(Auditor):
  GENDER_CHOICES = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('UNDEFINED', 'UNDEFINED'),
  ]
  
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  name = models.CharField(max_length=350)
  gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
  birth_date = models.DateField(null=True)
  document_number = models.CharField(max_length=50, blank=True, null=True)
  document_type = models.CharField(max_length=50, blank=True, null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons')