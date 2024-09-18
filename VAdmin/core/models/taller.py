from django.db import models


class Taller(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  email = models.EmailField()
  nit = models.CharField()
  description = models.TextField()