from django.db import models
from django.contrib.auth.models import User
from core.models import Auditor
import uuid

class Person(Auditor):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    first_lastname = models.CharField(max_length=50)
    second_lastname = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')