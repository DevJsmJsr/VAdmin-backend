from django.db import models

class Employee(models.Model):
  national_id = models.CharField(primary_key=True, max_length=50)
  name = models.CharField(max_length=100)