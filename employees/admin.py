from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('username', 'email', 'phone')
   list_per_page = 25
   readonly_fields = ('username', 'email', 'phone')

admin.site.register(Employee, EmployeeAdmin)
