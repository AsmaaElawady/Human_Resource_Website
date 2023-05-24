from django.db import models

# Create your models here.

class RegisterForm(models.Model):
    gndr=[
        ('Male','M'),('Female','F'),
        ]
    ms=[
        ('Single','Single'),('Married','Married'),
        ]
    stats=[
        ('Active','Active'),
        ('Inactive','Inactive'),
    ]
    EmployeeID = models.CharField(max_length=100,primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    Addres = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
    NumberVacation = models.CharField(max_length=100)
    NumberApprovedVacation = models.CharField(max_length=100)
    Date = models.DateField()
    Gender = models.CharField(max_length=8,choices=gndr)
    Status = models.CharField(max_length=8,choices=stats)
    MARITALSTATUE = models.CharField(max_length=8,choices=ms)

class VacationForm(models.Model):
    name = models.CharField(max_length = 50)
    ID = models.CharField(max_length = 50, primary_key = True)
    fromDate = models.DateField()
    toDate = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length = 15)


# class Upform(models.Model):
#     EmployeeID=models.CharField(max_length=100,primary_key=True)
#     EmployeeName=models.CharField(max_length=100)
