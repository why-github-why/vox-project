from django.db import models
from datetime import datetime

class Employee(models.Model):
   email = models.CharField(max_length=50)
   phone = models.CharField(max_length=20, blank=True)
   username = models.CharField(max_length=20)
   password = models.CharField(max_length=50)
   date_registered = models.DateTimeField(default=datetime.now, blank=True)

   def __str__(self):
      return self.username
