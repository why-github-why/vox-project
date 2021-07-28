from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
   username = models.CharField(max_length=200, default='Username', null=True)
   email = models.CharField(max_length=100, default='Email', null=True)
   phone = models.CharField(max_length=50)

   def __str__(self):
      return self.username.capitalize()
