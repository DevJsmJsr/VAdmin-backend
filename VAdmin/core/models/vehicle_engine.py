from django.db import models

class VehicleEngine(models.Model):
  transmission = models.CharField(max_length=100)
  horse_power = models.DecimalField(max_digits=5, decimal_places=2)
  engine_type = models.CharField(max_length=100)
  brake_system = models.CharField(max_length=100)
  vehicle = models.OneToOneField('core.Vehicle', on_delete=models.CASCADE, related_name='vehicle_engine')
