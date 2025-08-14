from django.contrib.postgres.fields import IntegerRangeField
from rest_framework.fields import CharField
from django.db import models

class Students(models.Model):
    student_id = models.CharField(max_length=10,unique=True)  # not primary key yet
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
       # Unique email
    def __str__(self):
        return f"{self.name}"

class Employee_details(models.Model):
    emp_id = models.CharField(max_length=20,unique=True)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()