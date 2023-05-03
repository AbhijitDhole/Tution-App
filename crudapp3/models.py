from django.db import models

# Create your models here.

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.s_id}---{self.name}----{self.address}"
    
class Courses(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=100)
    c_fees = models.CharField(max_length=20)
    date = models.DateField()
    
    