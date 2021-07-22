from django.db import models
from datetime import datetime

class Employee(models.Model):
   username = models.CharField(max_length=20)
   email = models.CharField(max_length=50, default='Email')
   phone = models.CharField(max_length=20, blank=True)
   date_registered = models.DateTimeField(default=datetime.now, blank=True)

   def __str__(self):
      return self.username
