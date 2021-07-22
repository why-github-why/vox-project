from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('id', 'username', 'email', 'phone', 'date_registered')
   list_display_links = ('id', 'username')
   search_fields = ('username', 'email')
   list_per_page = 25

admin.site.register(Employee, EmployeeAdmin)