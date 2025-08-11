from django.contrib.postgres.fields import IntegerRangeField
from rest_framework.fields import CharField
from django.db import models

class Student(models.Model):
    student_id = models.CharField(primary_key=True,max_length=10)  # Auto-increment ID
    name = models.CharField(max_length=100)          # Student name
    email = models.EmailField(unique=True)           # Unique email

    def __str__(self):
        return f"{self.name}"

class Employee_det(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name