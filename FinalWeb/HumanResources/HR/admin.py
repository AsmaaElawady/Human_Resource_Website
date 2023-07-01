from django.contrib import admin
from .models import RegisteredVacationForm
from .models import RegisterForm



# # Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("EmployeeID", "EmployeeName", "email","phone","Addres","Salary","NumberVacation","NumberApprovedVacation","Date","MARITALSTATUE",)
  
  
class MemberAdmin1(admin.ModelAdmin):
  list_display = ("VFName", "VFID", "VFFromDate","VFToDate","VFReason","VFStatus",)
    
admin.site.register(RegisteredVacationForm,MemberAdmin1)
admin.site.register(RegisterForm,MemberAdmin)