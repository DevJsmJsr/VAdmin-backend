from django.db import models
from auto_workshop.models import Garage

class Review(models.Model):
  detail = models.TextField()
  vehicle = models.ForeignKey('core.Vehicle', on_delete=models.CASCADE, related_name='vehicle_review')
  garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name='vehicle_review')
