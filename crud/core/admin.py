from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # docs: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('id', 'emp_name', 'emp_role', 'emp_salary')

# Register your models here.

# admin.site.register(Employee, EmployeeAdmin) # Use register decorator
