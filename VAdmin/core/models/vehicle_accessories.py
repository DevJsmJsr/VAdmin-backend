from django.db import models

class VehicleAccessories(models.Model):
  reverse_cam = models.BooleanField(default=False)
  sunroof = models.BooleanField(default=False)
  power_mirrors = models.BooleanField(default=False)
  power_seats = models.BooleanField(default=False)
  voice_control = models.BooleanField(default=False)
  driven_assistance = models.BooleanField(default=False)
  bluetooth = models.BooleanField(default=False)
  air_conditioning = models.BooleanField(default=False)
  cruise_control = models.BooleanField(default=False)
  parking_sensors = models.BooleanField(default=False)
  anti_theft_system = models.BooleanField(default=False)
  alarm_system = models.BooleanField(default=False)
  remote_start = models.BooleanField(default=False)
  vehicle = models.OneToOneField('core.Vehicle', on_delete=models.CASCADE, related_name='vehicle_engine')