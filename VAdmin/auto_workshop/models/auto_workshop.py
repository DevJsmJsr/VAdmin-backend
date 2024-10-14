from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AutoWorkshop(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  email = models.EmailField()
  nit = models.CharField()
  description = models.TextField()
  user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)