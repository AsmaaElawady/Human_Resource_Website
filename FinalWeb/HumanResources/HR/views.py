from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import RegisterForm 
# from .models import Upform 
from django.shortcuts import render

# def home(request):
#   if 1==1:
#     name=request.POST.get('EmployeeName')
#     return HttpResponse(name)
#   return render(request, 'phase1.html',{'mysorm':RegisterForm})
  
  
#     # return render(request, 'home.html')


def index(request):
  mymembers = RegisterForm.objects.all().values()
  # template = loader.get_template('phase1.html')
  template = loader.get_template('table.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
  
def add(request):
  template = loader.get_template('phase1.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  EmployeeID = request.POST['EmployeeID']
  EmployeeName = request.POST['EmployeeName']
  email = request.POST['email']
  phone = request.POST['phone']
  Addres = request.POST['Addres']
  Salary = request.POST['Salary']
  NumberVacation = request.POST['NumberVacation']
  NumberApprovedVacation = request.POST['NumberApprovedVacation']
  Date = request.POST['Date']
  Gender = request.POST['Gender']
  Status = request.POST['Status']
  MARITALSTATUE = request.POST['MARITALSTATUE']

  member = RegisterForm(EmployeeID=EmployeeID,EmployeeName=EmployeeName,email=email,phone=phone,Addres=Addres,Salary=Salary,NumberVacation=NumberVacation,NumberApprovedVacation=NumberApprovedVacation,Date=Date,Gender=Gender,Status=Status,MARITALSTATUE=MARITALSTATUE )
  member.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, EmployeeID):
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, EmployeeID):
  mymember = RegisterForm.objects.get(EmployeeID=EmployeeID)
  template = loader.get_template('editinfo.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, EmployeeID):
  EmployeeName = request.POST['EmployeeName']
  EmployeeID = request.POST['EmployeeID']
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)
  member.EmployeeName = EmployeeName
  member.EmployeeID = EmployeeID
  member.save()
  return HttpResponseRedirect(reverse('index'))














# #function to render the update page

# def update(request):
#     mymembers = RegisterForm.objects.all().values()
#     template = loader.get_template('update.html')
#     context = {
#       'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))
#   #  template = loader.get_template('update.html')
#   #  return HttpResponse(template.render({}, request))

# def updateEmp(request ):
#     template = loader.get_template('editinfo.html')
#     return HttpResponse(template.render({}, request))

#   #template = loader.get_template('editinfo.html')
#   #return HttpResponse(template.render({}, request))

# #function to get the values the user entered 
# #employee's data for which to update or delete




# # def delete(request, event_id):
# #     member = RegisterForm.objects.get(pk=event_id)
# #     member.delete()
# #     return HttpResponseRedirect(reverse('index'))
