from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now  # use instead of datetime.datetime.now


class Customer(models.Model):
   customer_id = models.CharField(max_length=25)  # IntegerField()
   company_name = models.CharField(max_length=50)
   customer_email = models.CharField(max_length=50)
   customer_phone = models.CharField(max_length=25, blank=True)
   customer_creation = models.DateTimeField(default=now, blank=True)  # auto_now_add=True
   user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)  # to_field="username"

   def __str__(self):
      return f"User: {self.user}, Customer ID: {self.customer_id}"
