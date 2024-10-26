from django.db import models
from core.models import Person

class Phone(models.Model):
  phone_number = models.CharField(max_length=15)
  person = models.ForeignKey(Person, related_name='phones', on_delete=models.CASCADE)
