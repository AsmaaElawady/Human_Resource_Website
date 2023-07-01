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
    NumberVacation = models.IntegerField()
    NumberApprovedVacation = models.IntegerField()
    Date = models.DateField()
    Gender = models.CharField(max_length=8,choices=gndr)
    Status = models.CharField(max_length=8,choices=stats)
    MARITALSTATUE = models.CharField(max_length=8,choices=ms)


def __str__(self):
    return f"{self.EmployeeName} {self.email} {self.phone} {self.Addres} {self.Salary} {self.NumberVacation} {self.NumberApprovedVacation}{self.Date}"



class RegisteredVacationForm(models.Model):
    VFName = models.CharField(max_length = 50)
    VFID = models.CharField(max_length = 50)
    VFFromDate = models.DateField()
    VFToDate = models.DateField()
    VFReason = models.TextField()
    VFStatus = models.CharField(max_length = 15)

def __str__(self):
    return f"{self.VFFromDate} {self.VFID} {self.VFFromDate} {self.VFToDate} {self.VFReason} {self.VFStatus} "

# class Upform(models.Model):
#     EmployeeID=models.CharField(max_length=100,primary_key=True)
#     EmployeeName=models.CharField(max_length=100)
