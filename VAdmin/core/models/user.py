from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Auditor


class User(AbstractUser, Auditor):
  USER='USER'
  AUTO_WORKSHOP='AUTO_WORKSHOP'
  
  ROL_CHOICES = [
    ('USER', 'USER'),
    ('AUTO_WORKSHOP', 'AUTO_WORKSHOP'),
  ]

  email = models.EmailField(unique=True)
  rol=models.CharField(max_length=14, choices=ROL_CHOICES)