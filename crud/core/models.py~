from django.db import models
import uuid

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=50)
    emp_salary = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    def __str__(self):
        return self.emp_name
    
