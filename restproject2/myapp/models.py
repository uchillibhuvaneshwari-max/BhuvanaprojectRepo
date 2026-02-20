from django.db import models

# Create your models here.
class Employee(models.Model):
      eno=models.IntegerField()
      ename=models.CharField(max_length=100)
      esal=models.DecimalField(max_digits=10,decimal_places=2)
      eaddr=models.CharField(max_length=100) 