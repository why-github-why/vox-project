from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
   list_display = ('user', 'customer_id', 'company_name', 'customer_email')
   list_display_links = ('user', 'customer_id', 'company_name')
   search_fields = ('user', 'customer_id', 'company_name')
   list_per_page = 25
   readonly_fields = ('user', 'customer_id', 'customer_creation')

admin.site.register(Customer, CustomerAdmin)
